
# 📝 Publications

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ISBI 2025</div><img src='images/egs.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[EG-SpikeFormer: Eye-Gaze Guided Transformer on Spiking Neural Networks for Medical Image Analysis](https://arxiv.org/pdf/2410.09674) \\
**Yi Pan**, Hanqi Jiang, Junhao Chen, Yiwei Li, Huaqin Zhao, Yifan Zhou, Peng Shu, Zihao Wu, Zhengliang Liu, Dajiang Zhu, Xiang Li, Yohannes Abate, Tianming Liu

<!-- [**Project**](https://speechresearch.github.io/fastspeech2/) <strong><span class='show_paper_citations' data='4FA6C0AAAAAJ:LkGwnXOMwfcC'></span></strong> -->
  - Neuromorphic computing has emerged as a promising energy-efficient alternative to traditional artificial neural networks (ANNs), predominantly utilizing spiking neural networks (SNNs) implemented on neuromorphic hardware. SNNs are more energy-efficient and excel at processing spatio-temporal data than ANNs. Significant advancements have been made in SNN-based convolutional neural networks (CNNs) and Transformer architectures. However, neuromorphic computing for the medical imaging domain remains underexplored. In this study, we introduce EG-SpikeFormer, an SNN architecture tailored for clinical tasks that incorporates eye-gaze data to guide the model's attention to the diagnostically relevant regions in medical images. Our developed approach effectively addresses shortcut learning issues commonly observed in conventional models, especially in scenarios with limited clinical data and high demands for model reliability, generalizability, and transparency. Our EG-SpikeFormer not only demonstrates superior energy efficiency and performance in medical image prediction tasks but also enhances clinical relevance through multi-modal information alignment. By incorporating eye-gaze data, the model improves interpretability and generalization, opening new directions for applying neuromorphic computing in medical image analysis.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICLR 2025</div><img src='images/pipeline_EchoPulse.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[ECHOPluse: ECG Controlled Echocardiograms Video Generation](https://arxiv.org/pdf/2410.03143) \\
Yiwei Li, Sekeun Kim, Zihao Wu, Hanqi Jiang, **Yi Pan**, Pengfei Jin, Sifan Song, Yucheng Shi, Xiaowei Yu, Tianze Yang, Tianming Liu, Quanzheng Li, Xiang Li

<!-- [**Project**](https://speechresearch.github.io/fastspeech2/) <strong><span class='show_paper_citations' data='4FA6C0AAAAAJ:LkGwnXOMwfcC'></span></strong> -->
  - We propose ECHOPluse, an ECG-conditioned ECHO video generation model. ECHOPluse introduces two key advancements: (1) it accelerates ECHO video generation by leveraging VQ-VAE tokenization and masked visual token modeling for fast decoding, and (2) it conditions on readily accessible ECG signals, which are highly coherent with ECHO videos, bypassing complex conditional prompts. To the best of our knowledge, this is the first work to use time-series prompts like ECG signals for ECHO video generation. ECHOPluse not only enables controllable synthetic ECHO data generation but also provides updated cardiac function information for disease monitoring and prediction beyond ECG alone. Evaluations on three public and private datasets demonstrate state-of-the-art performance in ECHO video generation across both qualitative and quantitative measures. Additionally, ECHOPluse can be easily generalized to other modality generation tasks, such as cardiac MRI, fMRI, and 3D CT generation. 
  - [Demo](https://github.com/levyisthebest/ECHOPulse_Prelease)
</div>
</div>