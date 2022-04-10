import os

from trainer import Trainer, TrainerArgs

from TTS.config.shared_configs import BaseAudioConfig
from TTS.tts.configs.shared_configs import BaseDatasetConfig
from TTS.tts.configs.tacotron2_config import Tacotron2Config
from TTS.tts.datasets import load_tts_samples
from TTS.tts.models.tacotron2 import Tacotron2
from TTS.tts.utils.text.tokenizer import TTSTokenizer
from TTS.utils.audio import AudioProcessor

# from TTS.tts.datasets.tokenizer import Tokenizer

output_path = os.path.dirname(os.path.abspath(__file__))

# init configs
dataset_config = BaseDatasetConfig(
    name="hakka", meta_file_train="metadata_train.csv", meta_file_val="metadata_val.csv", language="hakka", path=os.path.join(output_path, "../Hakka-0.9/")
)

audio_config = BaseAudioConfig(
    sample_rate=16000,
    do_trim_silence=True,
    trim_db=60.0,
    do_sound_norm=True,
    do_rms_norm=True,
    db_level=-20,
    signal_norm=True,
    mel_fmin=100.0,
    mel_fmax=4000,
    spec_gain=1.0,
    log_func="np.log",
    ref_level_db=20,
    preemphasis=0.0,
    stats_path="./scale_stats.npy",
)

config = Tacotron2Config(  # This is the config that is saved for the future use
    audio=audio_config,
    batch_size=64,
    eval_batch_size=64,
    num_loader_workers=4,
    num_eval_loader_workers=4,
    run_eval=True,
    test_delay_epochs=-1,
    r=6,
    gradual_training=[[0, 6, 64], [10000, 4, 32], [50000, 3, 32], [100000, 2, 32]],
    double_decoder_consistency=True,
    epochs=10000,
    text_cleaner="hakka_cleaners",
    use_phonemes=False,
    phoneme_language="hakka",
    phoneme_cache_path=os.path.join(output_path, "phoneme_cache"),
    precompute_num_workers=8,
    print_step=25,
    print_eval=True,
    save_n_checkpoints=10,
    save_all_best=True,
    mixed_precision=False,
    output_path=output_path,
    datasets=[dataset_config],
    test_sentences=[
        "ngai11 ham55 bun24 ng11 tang24: loi11 io24 !",
        "loi11 mai24 fan24 su11 io24 !",
        "ho31 siid5 ge55 fan24 su11 e31, fun31 iu55 tiam11 o31 !",
        "bau24 ng11 siid5 e11 van11 voi55 do55 zon31 loi11 mai24 io24 !",
        "loi11 mai24 coi55 o31 !",
        "id2 za24 siib5 ge55 ngiun11 tin55 tin55 .",
        "ia31 deu24 fa55 ngai11 qion11 gi55 cai55 xim24 ."
        ],
    max_decoder_steps = 1000,
)

# init audio processor
ap = AudioProcessor(**config.audio.to_dict())

# INITIALIZE THE AUDIO PROCESSOR
# Audio processor is used for feature extraction and audio I/O.
# It mainly serves to the dataloader and the training loggers.
ap = AudioProcessor.init_from_config(config)

# INITIALIZE THE TOKENIZER
# Tokenizer is used to convert text to sequences of token IDs.
# If characters are not defined in the config, default characters are passed to the config
tokenizer, config = TTSTokenizer.init_from_config(config)

# LOAD DATA SAMPLES
# Each sample is a list of ```[text, audio_file_path, speaker_name]```
# You can define your custom sample loader returning the list of samples.
# Or define your custom formatter and pass it to the `load_tts_samples`.
# Check `TTS.tts.datasets.load_tts_samples` for more details.
train_samples, eval_samples = load_tts_samples(dataset_config, eval_split=True)

# INITIALIZE THE MODEL
# Models take a config object and a speaker manager as input
# Config defines the details of the model like the number of layers, the size of the embedding, etc.
# Speaker manager is used by multi-speaker models.
model = Tacotron2(config, ap, tokenizer, speaker_manager=None)

# init the trainer and 🚀
trainer = Trainer(
    TrainerArgs(),
    config,
    output_path,
    model=model,
    train_samples=train_samples,
    eval_samples=eval_samples,
    training_assets={"audio_processor": ap},
)
trainer.fit()
