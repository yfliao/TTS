# 🐸💬 TTS Hakka Recipes

## Pre-trained "tacotron2-DDC" model

1. download the pre-trained model from https://drive.google.com/drive/folders/1zK6j2nmbGKV8q6rPQXbTI_MUtfqTOimT?usp=sharing
2. synthesis

* commandline
```
tts --text "ngai11 ham55 bun24 ng11 tang24 loi11 io24" --model_path best_model.pth --config_path config.json --out_path speech.wav
```
## Sample Voice

* https://drive.google.com/file/d/1Xqet4ht0QcNau0c-EH3LPJW_rkub4tCp/view?usp=sharing

## Remark

* To mitigate the impact of configuration inconsistencies between different recording sessions, some compromises have been made (mainly, mel_max=4000, please check the code or config.json).


* web server
```
 tts-server --model_path best_model.pth --config_path config.json
 http://[::1]:5002/
```

![image](https://github.com/yfliao/TTS/blob/main/recipes/hakka/%E5%9B%9B%E7%B8%A3%E8%85%94%E5%AE%A2%E8%AA%9E%E8%AA%9E%E9%9F%B3%E5%90%88%E6%88%90%E7%B6%B2%E9%A0%81%E5%9C%96.png)
