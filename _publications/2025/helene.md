---
title:          "HELENE: Hessian Layer-wise Clipping and Gradient Annealing for Accelerating Fine-tuning LLM with Zeroth-order Optimization"
date:           2025-08-20 15:00:00 -0400
selected:       true
pub:            "Empirical Methods in Natural Language Processing (EMNLP 2025)"
# pub_pre:        "Submitted to "
# pub_post:       'Under review.'
pub_last:       ' <span class="badge badge-pill badge-custom badge-secondary">Conference</span>'
pub_date:       "2025"

abstract: >-
  Fine-tuning large language models (LLMs) poses significant memory challenges, as the back-propagation process demands extensive resources, especially with growing model sizes. Recent work, MeZO, addresses this issue using a zeroth-order (ZO) optimization method, which reduces memory consumption by matching the usage to the inference phase. However, MeZO experiences slow convergence due to varying curvatures across model parameters. To overcome this limitation, we introduce HELENE, a novel scalable and memory-efficient optimizer that integrates annealed A-GNB gradients with a diagonal Hessian estimation and layer-wise clipping, serving as a second-order pre-conditioner. This combination allows for faster and more stable convergence. Our theoretical analysis demonstrates that HELENE improves convergence rates, particularly for models with heterogeneous layer dimensions, by reducing the dependency on the total parameter space dimension. Instead, the method scales with the largest layer dimension, making it highly suitable for modern LLM architectures. Experimental results on RoBERTa-large and OPT-1.3B across multiple tasks show that HELENE achieves up to a 20x speedup compared to MeZO, with average accuracy improvements of 1.5%. Furthermore, HELENE remains compatible with both full parameter tuning and parameter-efficient fine-tuning (PEFT), outperforming several state-of-the-art optimizers. The codes will be released after reviewing.

cover:          assets/images/covers/helene.jpg
authors:
  - Huaqin Zhao
  - Jiaxi Li
  - Yi Pan
  - Shizhe Liang
  - Xiaofeng Yang
  - Wei Liu
  - Xiang Li
  - Fei Dou
  - Tianming Liu
  - Jin Lu†
links:
  Paper: https://openreview.net/pdf?id=1vJXI67bIN
  Conference: https://2025.emnlp.org/
---
