---
title:          "MEDQUA: A NISQ-AWARE QUANTUM ADAPTER FOR MEDICAL VISION-LANGUAGE MODELS"
date:           2026-01-13 00:01:00 -0400
selected:       true
pub:            "IEEE International Symposium on Biomedical Imaging (ISBI 2026)"
pub_last:       ' <span class="badge badge-pill badge-custom badge-secondary">Conference</span>'
pub_date:       "2026"

abstract: >-
  Vision–language models (VLMs) are promising for medical image classification but still face generalization limits from visual encoders and cross-site distribution shift. Fully quantum VLMs could offer richer representations, yet NISQ hardware makes end-to-end quantum training impractical. We introduce MEDQUA, a NISQ-aware quantum adapter that attaches to a pretrained VLM decoder. An entropy-driven router sparsely selects tokens for a shallow variational quantum bottleneck, while a lightweight LoRA-based classical path processes all tokens to ensure stability and low cost. On MIMIC-CXR and ChestMNIST, MEDQUA consistently improves accuracy and AUROC over classical VLM baselines (including SFT) with modest overhead, showing that adaptively integrated quantum modules already yield practical gains.

cover:          assets/images/covers/medqua.png
authors:
  - Yiwei Li
  - Yi Pan
  - Junhao Chen
  - Yifan Zhou
  - Hanqi Jiang
  - Huaqin Zhao
  - Yanjun Lyu
  - Zhengliang Liu
  - Lin Zhao
  - Dajiang Zhu
  - Yingfeng Wang†
  - Tianming Liu†
links:
  Paper: assets/publications/2026/medqua.pdf
---
