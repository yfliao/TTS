# 🐸💬 TTS Hakka Recipes

## Install on "Ubuntu 20.04"
```
conda create --name coqui python=3.9
conda activate coqui
conda install pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch-nightly

cd "your path to clone the Hakka version of Coqui TTS"
git clone https://github.com/yfliao/TTS

cd TTS
pip install -e .
```

## Training
```
conda activate coqui

cd "your path to the Hakka version of Coqui TTS"
cd TTS/recipes/hakka/tacotron2-DDC

# to generate "config.json"
python train_tacotron_ddc.py # will crash. since there are no "scale_stats.npy" yet.

python ../../../TTS/bin/compute_statistics.py config.json scale_stats.npy
nohup python train_tacotron_ddc.py &> train_tacotron_ddc.py.log &

PS: To mitigate the impact of configuration inconsistencies between different recording sessions in the given Hakka corpus, some compromises have been made (mainly, mel_max=4000, please check the code or config.json).
```

## Synthesis using Pre-trained "tacotron2-DDC" model

1. download the pre-trained model from https://drive.google.com/drive/folders/1zK6j2nmbGKV8q6rPQXbTI_MUtfqTOimT?usp=sharing
2. commandline
```
tts --text "ngai11 ham55 bun24 ng11 tang24 loi11 io24" --model_path best_model.pth --config_path config.json --out_path speech.wav
```

## Sample Voice
* https://drive.google.com/file/d/1Xqet4ht0QcNau0c-EH3LPJW_rkub4tCp/view?usp=sharing

## Remark
* To mitigate the impact of configuration inconsistencies between different recording sessions, some compromises have been made (mainly, mel_max=4000, please check the code or config.json).


## Web server
```
 tts-server --model_path best_model.pth --config_path config.json
 http://[::1]:5002/
```
# <img src="https://github.com/yfliao/TTS/blob/main/recipes/hakka/%E5%9B%9B%E7%B8%A3%E8%85%94%E5%AE%A2%E8%AA%9E%E8%AA%9E%E9%9F%B3%E5%90%88%E6%88%90%E7%B6%B2%E9%A0%81%E5%9C%96.png" height="400"/>
