## NewcomerCandidate: Characterizing Contributions of a Novice Developers

### ABSTRACT

The ability of an Open Source Software (OSS) project to attract, onboard, and retain any newcomer is vital to its livelihood. Evidence suggests that there is an upsurge in novice developers joining social coding platforms such as GitHub. However, the extent to which these developers contribute to OSS projects is unknown. We execute the protocols of a registered report to study the activities of a  Newcomer OSS-Candidate, who is a novice developer that is new to social coding platform with the intention to onboard an OSS project. We use GitHub as a case platform, analyzing 171 identified Newcomer OSS-Candidates to characterize their GitHub activities in terms of the repositories, contributions, and onboarding. Results show that newcomers are likely to target software based repositories, i.e., 66%. We observe that their first contributions are mainly associated with development activities (commits) and maintenance activities (PRs). Results also show that Newcomer OSS-Candidates are less likely to practice social coding in terms of multiple authorship in their first contributions. Our results indicate that Newcomer OSS-Candidates do end up onboarding (i.e., 30% quantitative, 70% follow-up survey), confirming that finding a way to start is the most challenging barrier. The work provides evidence that novice developers to social coding platforms like GitHub have potential to onboard and contribute to OSS projects.

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

