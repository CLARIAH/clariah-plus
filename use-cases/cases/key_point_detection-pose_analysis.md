# Key point detection/pose analysis for Eye Jean Desmet collection through DANE

## Metadata

* **Status:**  Proposed
* **Type:** Specific and Generic
* **Work Package**: WP5
* **Research Coordinators:**  Nanne van Noord and Christian Olesen
* **Coordinators for CLARIAH:**  Jasmijn Van Gorp, Roeland Ordelman
* **Participating Institutes:** Netherlands Institute for Sound & Vision, Eye Filmmuseum, University of Amsterdam, Utrecht University
* **End-users**: film, media and performance scholars, Eye, NISV
* **Developers**: NISV
* **Interest Groups**: Audiovisual Processing
* **Task IDs**:

## Description

Methodologically, current film, media and performance studies research on film style, including acting, has relied heavily on manual annotation approaches and human re-enactment based on the Laban movement analysis (LMA) method in combination with video annotation software (Pearlman, 2009; Oyallon-Koloski & Williams, 2018, see also the research University of Illinois Urbana-Champaign’s Movement Visualization Lab; Ruszev, 2018). As such research requires fine-grained and labour-intensive annotation, they often remain limited to single films, or smaller corpora. Our pilot project offers new entry points for such research by allowing for exploring and browsing poses in a larger corpus. Early cinema is heavily influenced by traditions and practices from theatre (Szeto, 2014). This influence can for example be observed in the movements and poses of actors. Because subtle poses do not come across on a large stage, theatrically trained actors were used to exaggerating their movements to reach the audience. When actors and directors transitioned from theatre to film such practices transitioned along with them. With this research we investigate the use of pose detection algorithms to characterise movements in early cinema, to determine whether it is possible to discern developments in film genres and conventions of movement based on the poses of the authors. For instance, a common assumption is that Scandinavian, German and Italian dramas developed distinct acting styles that could be considered more cinematic in their use of cinematic space, while the acting styles of farces and comedies were considered as pertaining to popular, theatrical genres such as vaudeville. Hitherto, scholars have not studied such genres on a large scale using computational approaches and based on a diverse corpus consisting of multiple genres, such as the Desmet Collection, so as to be able to test and challenge such assumptions. This research project sets out to fill this gap by allowing for searching and browsing patterns in poses with the use of a Jupyter Notebook.

### What is the research about?

This project analyzes a historical film/media studies use case focussing on the development of acting in early cinema through the lens of pose detection. Beyond its primary focus on early cinema, the project also aims to offer a new basis for analyzing pose in other types of more recent AV materials.

### What problem is hindering the research?

State of the art pose detection algorithms perform well for modern material that is high quality, and typically born digital. For digitised archival material it can be challenging to get accurate detections, moreover, the manner in which a person dresses might also result in missed detections. For instance, for women in long dresses that obscure their legs, there might only be detections for their upper body. Nonetheless, this should only be a minor hindrance and it should still be possible to do this research.


### What is needed to do the research?

To describe pose information we extend the pose representation of Jammalamadaka et al. (2012) to include full body, rather than only upper body keypoints. Keypoints are annotations of specific points on a human body, typically focusing on joints or extremities (e.g., top of the head, nose, elbow, hip, foot), that make it possible to describe the pose that the body is in. For this project we use the automatic keypoint detector of the detectron2 framework (Wu et al., 2019). This detector is able to recognise upto 17 keypoints which makes it possible to capture a wide variety of poses. While the project is still ongoing, the initial analyses show that this keypoint detection approach is sufficiently robust such that it can be applied to historical material, highlighting the feasibility of using computer vision techniques for historical film analysis.


#### Data

Curated selection of films from the Jean Desmet Collection (Eye Filmmuseum).


#### Tools

- Resource Viewer
- Search
- Segmentation
- DANE
- Jupyter Notebook


### What software and services are involved?

- DANE: Keypoint detector of the detectron2 framework (Wu et al., 2019)

### How to evaluate this?

(How do we evaluate the solution to the problem?)

## References

References to related resources and publications and especially links to related use-cases:

* Szeto, K. Y. (2014). Theater and Film. Oxford University Press.
* Jenny Oyallon-Kololski & Mark Williams. (2018)  “Annotating FloLo: Utilizing Laban Movement Analysis in The Media Ecology Project.” Women and Silent Screen (Shanghai). China Film Press. 64–70
* Pearlman, Karen. (2009). Cutting Rhythms. Shaping the Film Edit. Burlington.
* Movement Visualization Lab: http://mvlab.org/research.html
* Ruszev, Szilvia. (2018). “Rhythmic Trajectories – Visualizing Cinematic Rhythms in Film Sequences.” Women Cutting Movies: Editors from East and Central Europe (ed. by Adelheid Heftberger and Ana Grgic). Special Issue of Apparatus. Film, Media and Digital Cultures in Central and Eastern Europe 7. DOI: http://dx.doi.org/10.17892/app.2018.0007.146
* Jammalamadaka, N., Zisserman, A., Eichner, M., Ferrari, V., & Jawahar, C. (2012). Video Retrieval by Mimicking Poses. In Proceedings of the 2nd ACM International Conference on Multimedia Retrieval.
* Yuxin Wu, Alexander Kirillov, Francisco Massa and Wan-Yen Lo, & Ross Girshick. (2019). Detectron2. https://github.com/facebookresearch/detectron2.
