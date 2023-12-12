# LatVis: Large-scale Task-specific Language Model for Low-resource Vietnamese Multi-document Summarization

### Introduction
We introduce LatVis, a large-scale task-specific language model that specifically pre-trained for Vietnamese multi-document summarization (MDS) task and a Vietnamese multi-document labeled dataset with ∼10,000 samples. To the best of our knowledge, we introduce one of the very first public larger-size MDS dataset and public language model that designed for Vietnamese MDS task and proves to be a potential approach for natural language processing tasks in less-resourced languages. 

### Model
We use the official code for PRIMERA [[1]](#1) and use our pipeline to make it be able to work on Vietnamese text summarization datasets. The model can support up to 16K tokens.

![image](pipeline.png)

### Dataset
At the early phase of this project, due to the lack of Vietnamese unlabeled multi-document dataset, we divided the Newscorpus [[7]](#7) into smaller parts and translated Newshead [[8]](#8)  using Google Translate API and ultilized it as our pretraining dataset. 

Below is the statistics of Vietnamese unlabeled dataset: 

| Dataset | Newscorpus | Newshead | 
| :----------- | :-----------: | :-----------: | 
| Total clusters | 5778893 | 314033 | 
| Total articles | 17847516 | 1065571 | 
| Average length per article |  154.03 | 2925.55 |
| Average number of entities per article | 4.87 | 23.67 | 

Currently, only three Vietnamese MDS datasets are available, posing a significant challenge for research advancement in this domain. These MDS datasets such as VMDS [[2]](#2), ViMs [[3]](#3), and VLSP [[4]](#4) seem to be quite small. Therefore, to enrich the Vietnamese multi-document datasets resource, we translated WCEP [[6]](#6) - a dataset for MDS consists of short, human-written summaries about news events using gpt-3.5-turbo-16k model from OpenAI and spent hours manually curating the dataset. 

Below is the statistics of Vietnamese unlabeled dataset: 

| Dataset | WCEP [[6]](#6) | vi-WCEP | 
| :----------- | :-----------: | :-----------: | 
| Number of documents | 10K | 10K | 
| Average number of documents per cluster |  9.1 | 9.1 |
| Average number of words per cluster | 3866 | 4696 | 
| Average number of words per summary | 28 | 40 | 

You can download our dataset: [vi-WCEP](https://drive.google.com/drive/folders/1agrHbDDSz8HAcLmQ1cBr1SSDYTZ9jEpG?usp=drive_link)

### Evaluation

At our very stage, we use Hugging Face [rouge score](https://huggingface.co/spaces/evaluate-metric/rouge) which is a wrapper around [Google Research reimplementation of ROUGE](https://github.com/google-research/google-research/tree/master/rouge) on VNDS [[5]](#5) - vietnamese benchmark for text summarization and our model achieves comparable performance with Vietnamese SOTA models. Later, we find out that the rouge scorer seem be to wrong with Vietnamese:

| Dataset | Rouge-1 F1 | Rouge-2 F1 | Rouge-L F1 | AVG.R F1 |
| :----------- | :-----------: | :-----------: | :-----------: | :-----------: |  
| VNDS [[5]](#5) | 63.01 | 33.38 | 42.74 | 46.38 | 

For evaluation, we use [rouge scorer](https://github.com/pltrdy/rouge). We save our checkpoint model based on AVG.R F1.

Below are achieved results on some Vietnamese labeled datasets: 

| Dataset | Rouge-1 F1 | Rouge-2 F1 | Rouge-L F1 | AVG.R F1 |
| :----------- | :-----------: | :-----------: | :-----------: | :-----------: |  
| VNDS [[5]](#5) (zero shot) | 63.01 | 33.38 | 42.74 | 46.38 | 
| VNDS [[5]](#5) | 63.01 | 33.38 | 42.74 | 46.38 | 
| vi-WCEP (zero shot) | 48.03 | 23.36 | 37.73 | 36.37 |
| vi-WCEP | 96.25 | 52.10 | 73.77 | 74.04 |

Benchmark:

| Dataset | Rouge-1 F1 | Rouge-2 F1 | Rouge-L F1 | AVG.R F1 |
| :----------- | :-----------: | :-----------: | :-----------: | :-----------: |  
| VNDS [[5]](#5) |  |  |  |  | 

### Future work

1. Crawl and build the large unlabeled Vietnamese multi-document dataset from scratch.
2. Upload source code, pretrained models.

    
### References
<a id="1">[1]</a> Wen Xiao, Iz Beltagy, Giuseppe Carenini, Arman Cohan. “PRIMERA: Pyramid-based Masked Sentence Pre-training for Multi-document Summarization”. In: Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics. Vol. 1. 2022, pp. 5245–5263.

<a id="2">[2]</a> Trần Mai Vũ, Vũ Trọng Hóa, Phí Văn Thủy, Lê Đức Trọng, Hà Quang Thụy. "VietnameseMDS
:200 Cụm văn bản tiếng Việt dùng cho tóm tắt đa văn bản"


<a id="3">[3]</a> Tran, Nhi-Thao and Nghiem, Minh-Quoc and Nguyen, Nhung TH and Nguyen, Ngan Luu-Thuy and Van Chi, Nam and Dinh, Dien. "ViMs: a high-quality Vietnamese dataset for abstractive multi-document summarization". In: Language Resources and Evaluation. Vol. 54, Num. 4, pp. 893-920. 2020.

<a id="4">[4]</a> Mai-Vu Tran, Hoang-Quynh Le, Duy-Cat Can, Quoc-An Nguyen. "VLSP 2022 – ABMUSU Challenge: Vietnamese Abstractive multi-document summarization". In Proceedings of the 9th International Workshop on Vietnamese Language and Speech Processing (VLSP 2022).

<a id="5">[5]</a> https://github.com/ThanhChinhBK/vietnews

<a id="6">[6]</a> Demian Gholipour Ghalandari, Chris Hokamp, Nghia-The Pham, John Glover, Georgiana Ifrim. "A Large-Scale Multi-Document Summarization Dataset from the Wikipedia Current Events Portal". In Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics.

<a id="7">[7]</a> https://github.com/binhvq/news-corpus

<a id="8">[8]</a> Gu, Xiaotao and Mao, Yuning and Han, Jiawei and Liu, Jialu and Yu, Hongkun and Wu, You and Yu, Cong and Finnie, Daniel and Zhai, Jiaqi and Zukoski, Nicholas. "Generating Representative Headlines for News Stories". Proc. of the the Web Conf. 2020


