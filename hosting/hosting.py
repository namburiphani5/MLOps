from huggingface_hub import HfApi
import os

hf_token = os.getenv("HF_TOKEN")
api = HfApi(token=os.getenv("HF_TOKEN"))
api.upload_folder(
    folder_path="mlops/deployment",     # the local folder containing your files
    repo_id="{hf_token}/Bank-Customer-Churn",          # the target repo
    repo_type="space",                      # dataset, model, or space
    path_in_repo="",                          # optional: subfolder path inside the repo
)
