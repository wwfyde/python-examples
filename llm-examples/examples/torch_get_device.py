import torch

device = torch.device(
    "cuda"
    if torch.cuda.is_available()
    else "mps"
    if torch.mps.is_available()
    else "cpu"
)  # noqa E501

print(f"Using device: {device}")
