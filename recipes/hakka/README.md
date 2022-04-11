# 🐸💬 TTS Hakka Recipes

## Pre-trained "tacotron2-DDC" model

1. download the pre-trained model from https://drive.google.com/drive/folders/1zK6j2nmbGKV8q6rPQXbTI_MUtfqTOimT?usp=sharing
2. synthesis

* commandline
```
tts --text "ngai11 ham55 bun24 ng11 tang24 loi11 io24" --model_path best_model.pth --config_path config.json --out_path speech.wav
```
* web
```
 tts-server --model_path best_model.pth --config_path config.json
 http://[::1]:5002/
```

## Sample Voice

* https://drive.google.com/file/d/1Xqet4ht0QcNau0c-EH3LPJW_rkub4tCp/view?usp=sharing

## Remark

* To mitigate the impact of configuration inconsistencies between different recording sessions, some compromises have been made (mainly, mel_max=4000, please check the code or config.json).
