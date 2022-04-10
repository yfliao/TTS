# 🐸💬 TTS Hakka Recipes

## Pre-trained model:

tts --text "ngai11 ham55 bun24 ng11 tang24 loi11 io24 ." --model_path run-April-08-2022_01+16AM-0cf3265a/best_model.pth --config_path run-April-08-2022_01+16AM-0cf3265a/config.json --out_path speech.wav

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
