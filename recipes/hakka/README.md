# 🐸💬 TTS Hakka Recipes

## Pre-trained "tacotron2-DDC" model

1. download the pre-trained model from https://drive.google.com/drive/folders/1zK6j2nmbGKV8q6rPQXbTI_MUtfqTOimT?usp=sharing
2. synthesis command

```
tts --text "ngai11 ham55 bun24 ng11 tang24 loi11 io24 ." --model_path tacotron2-DDC/best_model.pth --config_path tacotron2-DDC/config.json --out_path speech.wav
```
## Sample Voice

1. https://drive.google.com/file/d/1Xqet4ht0QcNau0c-EH3LPJW_rkub4tCp/view?usp=sharing


## For running the recipes

1. Prepare your own Hakka dataset.
2. Go to your desired model folder and run the training.

    Running Python files. (Choose the desired GPU ID for your run and set ```CUDA_VISIBLE_DEVICES```)
    ```terminal
    CUDA_VISIBLE_DEVICES="0" python train_modelX.py
    ```

    Running bash scripts.
    ```terminal
    bash run.sh
    ```

💡 Note that these runs are just templates to help you start training your first model. They are not optimized for the best
result. Double-check the configurations and feel free to share your experiments to find better parameters together 💪.
