
Webconf21-deepfakes-in-the-wild
## Deepfakes in the Wild: Detection and Analysis

This repository contains materials used in the paper titled [Deepfakes in the Wild: Detection and Analysis](https://arxiv.org/abs/2103.04263), published in the proceedings of the Web Conference (ACM WWW), 2021. Check out the presentation video for the paper [here](https://drive.google.com/file/d/1100nIF9nXlyKZpL1H_s9Gi5knZLOeKkT/view).

## Paper Abstract

AI-manipulated videos, commonly known as deepfakes, are an emerging problem. Recently, researchers in academia and industry have contributed several (self-created) benchmark deepfake datasets, and deepfake detection algorithms. However, little effort has gone towards understanding deepfake videos in the wild, leading to a limited understanding of the real-world applicability of research contributions in this space. Even if detection schemes are shown to perform well on existing datasets, it is unclear how well the methods generalize to real-world deepfakes. To bridge this gap in knowledge, we make the following contributions: First, we collect and present the largest dataset of deepfake videos in the wild, containing 1,869 videos from YouTube and Bilibili, and extract over 4.8M frames of content. Second, we present a comprehensive analysis of the growth patterns, popularity, creators, manipulation strategies, and production methods of deepfake content in the real-world. Third, we systematically evaluate existing defenses using our new dataset, and observe that they are not ready for deployment in the real-world. Fourth, we explore the potential for transfer learning schemes and competition-winning techniques to improve defenses.


## Dataset Statistics

| Datasets | #Videos  | #Frames | Total duration | Avg. Duration  |
| :----------: | :-: | :-: | :-----: | :-: |
| DF-W YouTube | 1062 | 2.9M | 30h 1m 12s | 1m 42s |
| DF-W Bilibili | 807 | 1.9M | 18h 48m 48s | 1m 24s |
| DF-W | 1869 | 4.8M | 48h 50m 00s | 1m 34s |

To fairly evaluate the functionality of each step in a detection pipeline, e.g., extracting faces and detecting on per face, we choose to not split/post-process/modify these videos in any way. All the videos are in its original form. All the videos are published on YouTube and Bilibili and can be viewed by the public.

DF-W YouTube samples           |  DF-W Bilibili samples
:-------------------------:|:-------------------------:
<img src="samples/sample1.png" width="500">|<img src="samples/sample2.png" width="500">

## Request and Download the dataset

In order to download Deep Fakes Dataset, please fill out the [Google form](https://docs.google.com/forms/d/e/1FAIpQLScrIbmoK12TnAdeMj9f33Xc-UD4YD5dPiXjPzLL3VoTEYYHOA/viewform?usp=sf_link) after reading and agreeing our License Agreement. Upon acceptance of your request, the download link will be sent to the provided e-mail address. For any questions or feedback, please e-mail <jmpu@vt.edu> with the subject [Question about the DF-W Dataset]. You may untar the tar.gz files containing the dataset as follows:

```bash
tar -xvzf XXX.tar.gz
```

## Video Privacy Statement

* All videos belong to their respective creators.

* All videos were originally published on YouTube and [Bilibili](https://www.bilibili.com/).

* The DF-W dataset is only to be used for research purposes.

* Once the above application form has been filled out, we will verify the applicant’s academic email address, academic affiliation, and other necessary information. We require a strict agreement to ensure that the dataset is used only for research purposes.

* The dataset download link will expire automatically in xxx days, after the email is sent to the applicant.

* If you are the video creator and some parts of the dataset affect you, you can contact us to remove them.

## Citation
```
@inproceedings{pu2021deepfake,
  title={Deepfake Videos in the Wild: Analysis and Detection},
  author={Pu, Jiameng and Mangaokar, Neal and Kelly, Lauren and Bhattacharya, Parantapa and Sundaram, Kavya and Javed, Mobin and Wang, Bolun and Viswanath, Bimal},
  booktitle={Proceedings of The Web Conference 2021},
  year={2021}
}
```


## License
[MIT](https://choosealicense.com/licenses/mit/)
