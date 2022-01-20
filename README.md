## NewcomerCandidate: Characterizing Contributions of a Novice Developers

### ABSTRACT

The ability of an Open Source Software (OSS) project to attract, onboard, and retain any newcomer is vital to its livelihood. Evidence suggests that more novice users are joining social coding platforms such as GitHub, however, the extent to which they contribute to OSS projects is unknown. We coin the term ‘Neecomer Candidate’ to describe a novice developer that is new to a social coding platform, with the intention to later onboard an OSS project. In this study, we execute the protocol of a registered report to track and classify contributions of a newcomerto the GitHub platform. Our results show that 66% of newcomer candidates target software repositories, with 43% commits classified as development activities such as initializing a repository. Furthermore, 60% of submitted Pull Requests are classified as management (i.e., formatting code, cleaning up, and documentation). We find that first contributions of newcomer candidates are solo (single author), and do not involve code modified (or that will be modified) by someone else. In terms of onboarding, our quantitative analysis showed that 49% of newcomer candidates started the onboarding process to OSS repositories. A follow-up survey supported this claim, showing that 70% of participants made OSS contributions, and cited the barrier of finding a way to start as a key demotivator to onboard. The study reveals insights on the OSS onboarding process on platforms like GitHub and provides potential avenues to assist such newcomers to make their first OSS contributions.

## Replication package Structure:
```
📁 Newcomer Candidate project/
├─ 📁 Data/
├─ 📁 Scripts/ 
├─ 📁 Survey/
─
```
## Contents:
  1. [Data](https://github.com/ifrazrehman/NewcomerCandidate/tree/master/data)- is a folder that contains the dataset for `Newcomer Candidate project`.
  2. [Scripts](https://github.com/ifrazrehman/NewcomerCandidate/tree/master/script)- is a folder that contains the all the codes. 
  3. [Survey](https://github.com/ifrazrehman/NewcomerCandidate/tree/master/survey)- is a folder that contains the survey obtained from participants.

## How to run:
  1. Clone the repository from [here](https://github.com/ifrazrehman/NewcomerCandidate.git) and the Dataset from [here](https://github.com/ifrazrehman/NewcomerCandidate/tree/master/data)
  2. Extract the files.
  3. Open `Jupyter Notebook` or `Python Spyder`.
  4. Copy any code and Set your working directory using 
                
                ```
                import os
                
                #Please specify your dataset directory. 
                os.chdir("..../Dataset/")
                ```

## Authors:
1. [IFraz Rehman](https://ifrazrehman.github.io/), Nara Institute of Science and Technology (NAIST), Nara, Japan.
2. [Dong Wang](https://dong-w.github.io/), Nara Institute of Science and Technology (NAIST), Nara, Japan.
3. [Raula Gaikovina Kula](https://raux.github.io/), Nara Institute of Science and Technology (NAIST), Nara, Japan.
4. [Takashi Ishio](https://takashi-ishio.github.io/), Nara Institute of Science and Technology (NAIST), Nara, Japan.
5. [Kenichi Matsumoto](http://isw3.naist.jp/Contents/Research/cs-05-en.html), Nara Institute of Science and Technology (NAIST), Nara, Japan.




## MIT License for code
Our SZZ implementation is licensed under the [MIT License](LICENSE).

## CC0 1.0 Universal for dataset
CC0 [summary](https://creativecommons.org/publicdomain/zero/1.0/) and [legal text](https://creativecommons.org/publicdomain/zero/1.0/legalcode)

Our dataset are published on the public domain, so that anyone may freely build upon, enhance and reuse the dataset for any purposes without restriction under copyright or database law.

