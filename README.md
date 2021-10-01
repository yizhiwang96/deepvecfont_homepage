# DeepVecFont
This is the homepage for SIGGRAPH 2021 Technical paper "DeepVecFont: Synthesizing High-quality Vector Fonts via Dual-modality Learning".
Authors: [Yizhi Wang](https://yizhiwang96.github.io/) and [Zhouhui Lian](https://www.icst.pku.edu.cn/zlian/). WICT, Peking University.
Paper: to be published soon
Code: [GitHub](https://github.com/yizhiwang96/deepvecfont)
Video: [link]()

## Introduction

![Teaser](imgs/teaser.svg)



## Abstract
Automatic font generation based on deep learning has aroused a lot of interest in the last decade. However, only a few recently-reported approaches are capable of directly generating vector glyphs and their results are still far from satisfactory. In this paper, we propose a novel method, DeepVecFont, to effectively resolve this problem. Using our method, for the first time, visually-pleasing vector glyphs whose quality and compactness are both comparable to human-designed ones can be automatically generated. The key idea of our DeepVecFont is to adopt the techniques of image synthesis, sequence modeling and differentiable rasterization to exhaustively exploit the dual-modality information (i.e., raster images and vector outlines) of vector fonts. 

The highlights of this paper are threefold. First, we design a dual-modality learning strategy which utilizes both image-aspect and sequence-aspect features of fonts to synthesize vector glyphs. Second, we provide a new generative paradigm to handle unstructured data (e.g., vector glyphs) by randomly sampling plausible synthesis results to get the optimal one which is further refined under the guidance of generated structured data (e.g., glyph images). Finally, qualitative and quantitative experiments conducted on a publicly-available dataset demonstrate that our method obtains high-quality synthesis results in the applications of vector font generation and interpolation, significantly outperforming the state of the art.

## Demo
### Few-shot generation
Given a few vector glyphs of a font as reference, our model generates the full **vector** font:

Input glyphs:
<div align=center>
	<img src="imgs/font_02/gt/02_00.svg"> 
	<img src="imgs/font_02/gt/02_01.svg"> 
	<img src="imgs/font_02/gt/02_26.svg"> 
	<img src="imgs/font_02/gt/02_27.svg"> 
</div>
Synthesized glyphs by DeepVecFont:
<div align=center>
	<img src="imgs/font_02/syn/02_00.svg"> 
	<img src="imgs/font_02/syn/02_01.svg"> 
	<img src="imgs/font_02/syn/02_02.svg"> 
	<img src="imgs/font_02/syn/02_03.svg"> 
	<img src="imgs/font_02/syn/02_04.svg">
	<img src="imgs/font_02/syn/02_05.svg">
	<img src="imgs/font_02/syn/02_06.svg">
	<img src="imgs/font_02/syn/02_07.svg"> 
	<img src="imgs/font_02/syn/02_08.svg"> 
	<img src="imgs/font_02/syn/02_09.svg"> 
	<img src="imgs/font_02/syn/02_10.svg"> 
	<img src="imgs/font_02/syn/02_11.svg">
	<img src="imgs/font_02/syn/02_12.svg">
	<img src="imgs/font_02/syn/02_13.svg">
	<img src="imgs/font_02/syn/02_14.svg"> 
	<img src="imgs/font_02/syn/02_15.svg"> 
	<img src="imgs/font_02/syn/02_16.svg"> 
	<img src="imgs/font_02/syn/02_17.svg"> 
	<img src="imgs/font_02/syn/02_18.svg">
	<img src="imgs/font_02/syn/02_19.svg">
	<img src="imgs/font_02/syn/02_20.svg">
	<img src="imgs/font_02/syn/02_21.svg"> 
	<img src="imgs/font_02/syn/02_22.svg"> 
	<img src="imgs/font_02/syn/02_23.svg"> 	
	<img src="imgs/font_02/syn/02_24.svg">
	<img src="imgs/font_02/syn/02_25.svg">
	<br/>
	<img src="imgs/font_02/syn/02_26.svg"> 
	<img src="imgs/font_02/syn/02_27.svg"> 
	<img src="imgs/font_02/syn/02_28.svg"> 
	<img src="imgs/font_02/syn/02_29.svg"> 
	<img src="imgs/font_02/syn/02_30.svg">
	<img src="imgs/font_02/syn/02_31.svg">
	<img src="imgs/font_02/syn/02_32.svg">
	<img src="imgs/font_02/syn/02_33.svg"> 
	<img src="imgs/font_02/syn/02_34.svg"> 
	<img src="imgs/font_02/syn/02_35.svg"> 
	<img src="imgs/font_02/syn/02_36.svg"> 
	<img src="imgs/font_02/syn/02_37.svg">
	<img src="imgs/font_02/syn/02_38.svg">
	<img src="imgs/font_02/syn/02_39.svg">
	<img src="imgs/font_02/syn/02_40.svg"> 
	<img src="imgs/font_02/syn/02_41.svg"> 
	<img src="imgs/font_02/syn/02_42.svg"> 
	<img src="imgs/font_02/syn/02_43.svg"> 
	<img src="imgs/font_02/syn/02_44.svg">
	<img src="imgs/font_02/syn/02_45.svg">
	<img src="imgs/font_02/syn/02_46.svg">
	<img src="imgs/font_02/syn/02_47.svg"> 
	<img src="imgs/font_02/syn/02_48.svg"> 
	<img src="imgs/font_02/syn/02_49.svg">
	<img src="imgs/font_02/syn/02_50.svg">
	<img src="imgs/font_02/syn/02_51.svg">	
	<br/>
</div>

Input glyphs:
<div align=center>
	<img src="imgs/font_12/gt/12_00.svg"> 
	<img src="imgs/font_12/gt/12_01.svg"> 
	<img src="imgs/font_12/gt/12_26.svg"> 
	<img src="imgs/font_12/gt/12_27.svg"> 
</div>
Synthesized glyphs by DeepVecFont:
<div align=center>
	<img src="imgs/font_12/syn/12_00.svg"> 
	<img src="imgs/font_12/syn/12_01.svg"> 
	<img src="imgs/font_12/syn/12_02.svg"> 
	<img src="imgs/font_12/syn/12_03.svg"> 
	<img src="imgs/font_12/syn/12_04.svg">
	<img src="imgs/font_12/syn/12_05.svg">
	<img src="imgs/font_12/syn/12_06.svg">
	<img src="imgs/font_12/syn/12_07.svg"> 
	<img src="imgs/font_12/syn/12_08.svg"> 
	<img src="imgs/font_12/syn/12_09.svg"> 
	<img src="imgs/font_12/syn/12_10.svg"> 
	<img src="imgs/font_12/syn/12_11.svg">
	<img src="imgs/font_12/syn/12_12.svg">
	<img src="imgs/font_12/syn/12_13.svg">
	<img src="imgs/font_12/syn/12_14.svg"> 
	<img src="imgs/font_12/syn/12_15.svg"> 
	<img src="imgs/font_12/syn/12_16.svg"> 
	<img src="imgs/font_12/syn/12_17.svg"> 
	<img src="imgs/font_12/syn/12_18.svg">
	<img src="imgs/font_12/syn/12_19.svg">
	<img src="imgs/font_12/syn/12_20.svg">
	<img src="imgs/font_12/syn/12_21.svg"> 
	<img src="imgs/font_12/syn/12_22.svg"> 
	<img src="imgs/font_12/syn/12_23.svg"> 	
	<img src="imgs/font_12/syn/12_24.svg">
	<img src="imgs/font_12/syn/12_25.svg">
	<br/>
	<img src="imgs/font_12/syn/12_26.svg"> 
	<img src="imgs/font_12/syn/12_27.svg"> 
	<img src="imgs/font_12/syn/12_28.svg"> 
	<img src="imgs/font_12/syn/12_29.svg"> 
	<img src="imgs/font_12/syn/12_30.svg">
	<img src="imgs/font_12/syn/12_31.svg">
	<img src="imgs/font_12/syn/12_32.svg">
	<img src="imgs/font_12/syn/12_33.svg"> 
	<img src="imgs/font_12/syn/12_34.svg"> 
	<img src="imgs/font_12/syn/12_35.svg"> 
	<img src="imgs/font_12/syn/12_36.svg"> 
	<img src="imgs/font_12/syn/12_37.svg">
	<img src="imgs/font_12/syn/12_38.svg">
	<img src="imgs/font_12/syn/12_39.svg">
	<img src="imgs/font_12/syn/12_40.svg"> 
	<img src="imgs/font_12/syn/12_41.svg"> 
	<img src="imgs/font_12/syn/12_42.svg"> 
	<img src="imgs/font_12/syn/12_43.svg"> 
	<img src="imgs/font_12/syn/12_44.svg">
	<img src="imgs/font_12/syn/12_45.svg">
	<img src="imgs/font_12/syn/12_46.svg">
	<img src="imgs/font_12/syn/12_47.svg"> 
	<img src="imgs/font_12/syn/12_48.svg"> 
	<img src="imgs/font_12/syn/12_49.svg">
	<img src="imgs/font_12/syn/12_50.svg">
	<img src="imgs/font_12/syn/12_51.svg">	
	<br/>
</div>

Input glyphs:
<div align=center>
	<img src="imgs/font_41/gt/41_00.svg"> 
	<img src="imgs/font_41/gt/41_01.svg"> 
	<img src="imgs/font_41/gt/41_26.svg"> 
	<img src="imgs/font_41/gt/41_27.svg"> 
</div>
Synthesized glyphs by DeepVecFont:
<div align=center>
	<img src="imgs/font_41/syn/41_00.svg"> 
	<img src="imgs/font_41/syn/41_01.svg"> 
	<img src="imgs/font_41/syn/41_02.svg"> 
	<img src="imgs/font_41/syn/41_03.svg"> 
	<img src="imgs/font_41/syn/41_04.svg">
	<img src="imgs/font_41/syn/41_05.svg">
	<img src="imgs/font_41/syn/41_06.svg">
	<img src="imgs/font_41/syn/41_07.svg"> 
	<img src="imgs/font_41/syn/41_08.svg"> 
	<img src="imgs/font_41/syn/41_09.svg"> 
	<img src="imgs/font_41/syn/41_10.svg"> 
	<img src="imgs/font_41/syn/41_11.svg">
	<img src="imgs/font_41/syn/41_12.svg">
	<img src="imgs/font_41/syn/41_13.svg">
	<img src="imgs/font_41/syn/41_14.svg"> 
	<img src="imgs/font_41/syn/41_15.svg"> 
	<img src="imgs/font_41/syn/41_16.svg"> 
	<img src="imgs/font_41/syn/41_17.svg"> 
	<img src="imgs/font_41/syn/41_18.svg">
	<img src="imgs/font_41/syn/41_19.svg">
	<img src="imgs/font_41/syn/41_20.svg">
	<img src="imgs/font_41/syn/41_21.svg"> 
	<img src="imgs/font_41/syn/41_22.svg"> 
	<img src="imgs/font_41/syn/41_23.svg"> 	
	<img src="imgs/font_41/syn/41_24.svg">
	<img src="imgs/font_41/syn/41_25.svg">
	<br/>
	<img src="imgs/font_41/syn/41_26.svg"> 
	<img src="imgs/font_41/syn/41_27.svg"> 
	<img src="imgs/font_41/syn/41_28.svg"> 
	<img src="imgs/font_41/syn/41_29.svg"> 
	<img src="imgs/font_41/syn/41_30.svg">
	<img src="imgs/font_41/syn/41_31.svg">
	<img src="imgs/font_41/syn/41_32.svg">
	<img src="imgs/font_41/syn/41_33.svg"> 
	<img src="imgs/font_41/syn/41_34.svg"> 
	<img src="imgs/font_41/syn/41_35.svg"> 
	<img src="imgs/font_41/syn/41_36.svg"> 
	<img src="imgs/font_41/syn/41_37.svg">
	<img src="imgs/font_41/syn/41_38.svg">
	<img src="imgs/font_41/syn/41_39.svg">
	<img src="imgs/font_41/syn/41_40.svg"> 
	<img src="imgs/font_41/syn/41_41.svg"> 
	<img src="imgs/font_41/syn/41_42.svg"> 
	<img src="imgs/font_41/syn/41_43.svg"> 
	<img src="imgs/font_41/syn/41_44.svg">
	<img src="imgs/font_41/syn/41_45.svg">
	<img src="imgs/font_41/syn/41_46.svg">
	<img src="imgs/font_41/syn/41_47.svg"> 
	<img src="imgs/font_41/syn/41_48.svg"> 
	<img src="imgs/font_41/syn/41_49.svg">
	<img src="imgs/font_41/syn/41_50.svg">
	<img src="imgs/font_41/syn/41_51.svg">	
	<br/>
</div>

## Citation:

If you use this code or find our work is helpful, please consider citing our work
