
# 📝 Publications

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICLR 2025</div><img src='images/pipeline_EchoPulse.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[ECHOPluse: ECG Controlled Echocardiograms Video Generation](https://arxiv.org/pdf/2410.03143) \\
Yiwei Li, Sekeun Kim, Zihao Wu, Hanqi Jiang, **Yi Pan**, Pengfei Jin, Sifan Song, Yucheng Shi, Xiaowei Yu, Tianze Yang, Tianming Liu, Quanzheng Li, Xiang Li

<!-- [**Project**](https://speechresearch.github.io/fastspeech2/) <strong><span class='show_paper_citations' data='4FA6C0AAAAAJ:LkGwnXOMwfcC'></span></strong> -->
  - We propose ECHOPluse, an ECG-conditioned ECHO video generation model. ECHOPluse introduces two key advancements: (1) it accelerates ECHO video generation by leveraging VQ-VAE tokenization and masked visual token modeling for fast decoding, and (2) it conditions on readily accessible ECG signals, which are highly coherent with ECHO videos, bypassing complex conditional prompts. To the best of our knowledge, this is the first work to use time-series prompts like ECG signals for ECHO video generation. ECHOPluse not only enables controllable synthetic ECHO data generation but also provides updated cardiac function information for disease monitoring and prediction beyond ECG alone. Evaluations on three public and private datasets demonstrate state-of-the-art performance in ECHO video generation across both qualitative and quantitative measures. Additionally, ECHOPluse can be easily generalized to other modality generation tasks, such as cardiac MRI, fMRI, and 3D CT generation. 
  - [Demo](https://github.com/levyisthebest/ECHOPulse_Prelease)
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ISBI 2025</div><img src='images/egs.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[EG-SpikeFormer: Eye-Gaze Guided Transformer on Spiking Neural Networks for Medical Image Analysis](https://arxiv.org/pdf/2410.09674) \\
**Yi Pan**, Hanqi Jiang, Junhao Chen, Yiwei Li, Huaqin Zhao, Yifan Zhou, Peng Shu, Zihao Wu, Zhengliang Liu, Dajiang Zhu, Xiang Li, Yohannes Abate, Tianming Liu

<!-- [**Project**](https://speechresearch.github.io/fastspeech2/) <strong><span class='show_paper_citations' data='4FA6C0AAAAAJ:LkGwnXOMwfcC'></span></strong> -->
  - we propose a novel gaze-guided spike-driven hybrid model EG-SpikeFormer for medical diagnosis for the first time, which integrates the low-power computation benefits of SNN with the powerful feature extraction capabilities of Transformers. The model incorporates radiologists' eye-gaze data as prior information during training, effectively guiding the model's attention. Our experiments on two public medical datasets demonstrate the model's superior performance in both energy efficiency and diagnostic accuracy. To the best of our knowledge, this is the first attempt to introduce a hybrid SNN model combining CNN and Transformer in the field of medical diagnosis, leveraging both low power consumption and strong interpretability. By incorporating radiologists' prior information during training, the model learns to focus on disease-relevant regions, reducing irrelevant information and significantly improving performance and interpretability in medical image diagnosis tasks. We also firstly propose a hardware-aware co-design framework that integrates neuromorphic computing and eye-gaze guidance, addressing medical challenges such as shortcut learning and data scarcity. This collaborative design not only enhances diagnostic accuracy and energy efficiency but also underscores the significance of such synergies in advancing practical healthcare applications.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">IEEE TNNLS</div><img src='images/maskvit
.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Mask-Guided Vision Transformer for Few-Shot Learning](https://ieeexplore.ieee.org/abstract/document/10589307) \\
Yuzhong Chen, Zhenxiang Xiao, **Yi Pan**, Lin Zhao, Haixing Dai, Zihao Wu, Changhe Li, Tuo Zhang, Changying Li, Dajiang Zhu, Tianming Liu, Xi Jiang

<!-- [**Project**](https://speechresearch.github.io/fastspeech2/) <strong><span class='show_paper_citations' data='4FA6C0AAAAAJ:LkGwnXOMwfcC'></span></strong> -->
  - We propose a novel MG-ViT to guide ViT more effectivelyand efficiently learn from the task-relevant prior knowledge for FSL. By simply adding an image patch mask operation and a residual connection to the vanilla ViT, MG-ViT significantly outperforms the general fine-tuning-based methods for FSL. To further improve the efficiency of FSL, we also introduce an effective active learning-based few-shot sample selection method. Our two-stage fine-tuning-based framework could be widely applied to different downstream tasks, such as image classification, object detection, and segmentation in this study. In general, MG-ViT provides a concrete approach toward generalizing data-intensive and large-scale deep learning models for FSL.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Information Fusion</div><img src='images/instructvit.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Instruction-ViT: Multi-modal prompts for instruction learning in vision transformer](https://www.sciencedirect.com/science/article/pii/S1566253523005201) \\
Zhenxiang Xiao, Yuzhong Chen, Junjie Yao, Lu Zhang, Zhengliang Liu, Zihao Wu, Xiaowei Yu, **Yi Pan**, Lin Zhao, Chong Ma, Xinyu Liu, Wei Liu, Xiang Li, Yixuan Yuan, Dinggang Shen, Dajiang Zhu, Dezhong Yao, Tianming Liu, Xi Jiang

<!-- [**Project**](https://speechresearch.github.io/fastspeech2/) <strong><span class='show_paper_citations' data='4FA6C0AAAAAJ:LkGwnXOMwfcC'></span></strong> -->
  - We propose Instruction-ViT, a simple and effective approach that aligns the input and prompts across distinct modalities. It leverages the pre-trained parameters from ViT-B as the backbone, and combines them with CLIP encoders as well as a flexible head module to complete various downstream tasks including image classification, segmentation, image captioning, and object detection. We show that Instruction-ViT can effectively use uni-modal prompts (e.g., images or texts) as well as multi-modal prompts (e.g., combined image and text features). Experimental results demonstrate that Instruction-ViT enhances the performance of the ViT-based model by incorporating prompts in different modalities, which can further improve the effectiveness of model with fewer parameter training requirements.
</div>
</div>