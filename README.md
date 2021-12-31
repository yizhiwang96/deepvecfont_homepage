# DeepVecFont
![Teaser](imgs/teaser.svg)

This is the homepage for "DeepVecFont: Synthesizing High-quality Vector Fonts via Dual-modality Learning". [Yizhi Wang](https://yizhiwang96.github.io/) and [Zhouhui Lian](https://www.icst.pku.edu.cn/zlian/). WICT, Peking University.

**Paper:** [**Arxiv**](https://arxiv.org/abs/2110.06688)

**Supplementary:** [**Link**](./pdfs/deepvecfont_sm.pdf)

**Code:** [**GitHub**](https://github.com/yizhiwang96/deepvecfont)

Video: 
<div align=center>
<video width="800" height="450" controls="controls">
  <source src="imgs/dvf_ff_v2.1.mp4" type="video/mp4" />
</video>
</div>

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

### Vector font interpolation
Rendered:
<div align=center>
	<img src="imgs/font_35_raw/syn/18.svg"> 
	<img src="imgs/font_35_raw/syn/08.svg"> 
	<img src="imgs/font_35_raw/syn/06.svg"> 
	<img src="imgs/font_35_raw/syn/06.svg">
	<img src="imgs/font_35_raw/syn/17.svg">
	<img src="imgs/font_35_raw/syn/00.svg">
	<img src="imgs/font_35_raw/syn/15.svg"> 
	<img src="imgs/font_35_raw/syn/07.svg">
	<img src="imgs/font_35_raw/syn/21.svg"> 
	<img src="imgs/font_35_raw/syn/30.svg"> 
	<img src="imgs/font_35_raw/syn/28.svg"> 
	<img src="imgs/font_35_raw/syn/05.svg"> 
	<img src="imgs/font_35_raw/syn/40.svg">
	<img src="imgs/font_35_raw/syn/39.svg"> 
	<img src="imgs/font_35_raw/syn/45.svg"> 
	<br/>
	<img src="imgs/font_35_57_3_raw/syn/18.svg"> 
	<img src="imgs/font_35_57_3_raw/syn/08.svg"> 
	<img src="imgs/font_35_57_3_raw/syn/06.svg"> 
	<img src="imgs/font_35_57_3_raw/syn/06.svg">
	<img src="imgs/font_35_57_3_raw/syn/17.svg">
	<img src="imgs/font_35_57_3_raw/syn/00.svg">
	<img src="imgs/font_35_57_3_raw/syn/15.svg"> 
	<img src="imgs/font_35_57_3_raw/syn/07.svg">
	<img src="imgs/font_35_57_3_raw/syn/21.svg"> 
	<img src="imgs/font_35_57_3_raw/syn/30.svg"> 
	<img src="imgs/font_35_57_3_raw/syn/28.svg"> 
	<img src="imgs/font_35_57_3_raw/syn/05.svg"> 
	<img src="imgs/font_35_57_3_raw/syn/40.svg">
	<img src="imgs/font_35_57_3_raw/syn/39.svg"> 
	<img src="imgs/font_35_57_3_raw/syn/45.svg"> 
	<br/>
	<img src="imgs/font_35_57_5_raw/syn/18.svg"> 
	<img src="imgs/font_35_57_5_raw/syn/08.svg"> 
	<img src="imgs/font_35_57_5_raw/syn/06.svg"> 
	<img src="imgs/font_35_57_5_raw/syn/06.svg">
	<img src="imgs/font_35_57_5_raw/syn/17.svg">
	<img src="imgs/font_35_57_5_raw/syn/00.svg">
	<img src="imgs/font_35_57_5_raw/syn/15.svg"> 
	<img src="imgs/font_35_57_5_raw/syn/07.svg"> 
	<img src="imgs/font_35_57_5_raw/syn/21.svg"> 
	<img src="imgs/font_35_57_5_raw/syn/30.svg"> 
	<img src="imgs/font_35_57_5_raw/syn/28.svg"> 
	<img src="imgs/font_35_57_5_raw/syn/05.svg"> 
	<img src="imgs/font_35_57_5_raw/syn/40.svg">
	<img src="imgs/font_35_57_5_raw/syn/39.svg"> 
	<img src="imgs/font_35_57_5_raw/syn/45.svg"> 
	<br/>
	<img src="imgs/font_35_57_7_raw/syn/18.svg"> 
	<img src="imgs/font_35_57_7_raw/syn/08.svg"> 
	<img src="imgs/font_35_57_7_raw/syn/06.svg"> 
	<img src="imgs/font_35_57_7_raw/syn/06.svg">
	<img src="imgs/font_35_57_7_raw/syn/17.svg">
	<img src="imgs/font_35_57_7_raw/syn/00.svg">
	<img src="imgs/font_35_57_7_raw/syn/15.svg"> 
	<img src="imgs/font_35_57_7_raw/syn/07.svg">
	<img src="imgs/font_35_57_7_raw/syn/21.svg"> 
	<img src="imgs/font_35_57_7_raw/syn/30.svg"> 
	<img src="imgs/font_35_57_7_raw/syn/28.svg"> 
	<img src="imgs/font_35_57_7_raw/syn/05.svg"> 
	<img src="imgs/font_35_57_7_raw/syn/40.svg">
	<img src="imgs/font_35_57_7_raw/syn/39.svg"> 
	<img src="imgs/font_35_57_7_raw/syn/45.svg"> 
	<br/>
	<img src="imgs/font_57_raw/syn/18.svg"> 
	<img src="imgs/font_57_raw/syn/08.svg"> 
	<img src="imgs/font_57_raw/syn/06.svg"> 
	<img src="imgs/font_57_raw/syn/06.svg">
	<img src="imgs/font_57_raw/syn/17.svg">
	<img src="imgs/font_57_raw/syn/00.svg">
	<img src="imgs/font_57_raw/syn/15.svg"> 
	<img src="imgs/font_57_raw/syn/07.svg">
	<img src="imgs/font_57_raw/syn/21.svg"> 
	<img src="imgs/font_57_raw/syn/30.svg"> 
	<img src="imgs/font_57_raw/syn/28.svg"> 
	<img src="imgs/font_57_raw/syn/05.svg"> 
	<img src="imgs/font_57_raw/syn/40.svg">
	<img src="imgs/font_57_raw/syn/39.svg"> 
	<img src="imgs/font_57_raw/syn/45.svg"> 
	<br/>
</div>
Outlines:
<div align=center>
	<img src="imgs/font_35/syn/35_18.svg"> 
	<img src="imgs/font_35/syn/35_08.svg"> 
	<img src="imgs/font_35/syn/35_06.svg"> 
	<img src="imgs/font_35/syn/35_06.svg">
	<img src="imgs/font_35/syn/35_17.svg">
	<img src="imgs/font_35/syn/35_00.svg">
	<img src="imgs/font_35/syn/35_15.svg"> 
	<img src="imgs/font_35/syn/35_07.svg">
	<img src="imgs/font_35/syn/35_21.svg"> 
	<img src="imgs/font_35/syn/35_30.svg"> 
	<img src="imgs/font_35/syn/35_28.svg"> 
	<img src="imgs/font_35/syn/35_05.svg"> 
	<img src="imgs/font_35/syn/35_40.svg">
	<img src="imgs/font_35/syn/35_39.svg"> 
	<img src="imgs/font_35/syn/35_45.svg"> 
	<br/>
	<img src="imgs/font_35_57_3/syn/35_57_3_18.svg"> 
	<img src="imgs/font_35_57_3/syn/35_57_3_08.svg"> 
	<img src="imgs/font_35_57_3/syn/35_57_3_06.svg"> 
	<img src="imgs/font_35_57_3/syn/35_57_3_06.svg">
	<img src="imgs/font_35_57_3/syn/35_57_3_17.svg">
	<img src="imgs/font_35_57_3/syn/35_57_3_00.svg">
	<img src="imgs/font_35_57_3/syn/35_57_3_15.svg"> 
	<img src="imgs/font_35_57_3/syn/35_57_3_07.svg"> 	
	<img src="imgs/font_35_57_3/syn/35_57_3_21.svg"> 
	<img src="imgs/font_35_57_3/syn/35_57_3_30.svg"> 
	<img src="imgs/font_35_57_3/syn/35_57_3_28.svg"> 
	<img src="imgs/font_35_57_3/syn/35_57_3_05.svg"> 
	<img src="imgs/font_35_57_3/syn/35_57_3_40.svg">
	<img src="imgs/font_35_57_3/syn/35_57_3_39.svg"> 
	<img src="imgs/font_35_57_3/syn/35_57_3_45.svg"> 
	<br/>
	<img src="imgs/font_35_57_5/syn/35_57_5_18.svg"> 
	<img src="imgs/font_35_57_5/syn/35_57_5_08.svg"> 
	<img src="imgs/font_35_57_5/syn/35_57_5_06.svg"> 
	<img src="imgs/font_35_57_5/syn/35_57_5_06.svg">
	<img src="imgs/font_35_57_5/syn/35_57_5_17.svg">
	<img src="imgs/font_35_57_5/syn/35_57_5_00.svg">
	<img src="imgs/font_35_57_5/syn/35_57_5_15.svg"> 
	<img src="imgs/font_35_57_5/syn/35_57_5_07.svg"> 
	<img src="imgs/font_35_57_5/syn/35_57_5_21.svg"> 
	<img src="imgs/font_35_57_5/syn/35_57_5_30.svg"> 
	<img src="imgs/font_35_57_5/syn/35_57_5_28.svg"> 
	<img src="imgs/font_35_57_5/syn/35_57_5_05.svg"> 
	<img src="imgs/font_35_57_5/syn/35_57_5_40.svg">
	<img src="imgs/font_35_57_5/syn/35_57_5_39.svg"> 
	<img src="imgs/font_35_57_5/syn/35_57_5_45.svg">	
	<br/>
	<img src="imgs/font_35_57_7/syn/35_57_7_18.svg"> 
	<img src="imgs/font_35_57_7/syn/35_57_7_08.svg"> 
	<img src="imgs/font_35_57_7/syn/35_57_7_06.svg"> 
	<img src="imgs/font_35_57_7/syn/35_57_7_06.svg">
	<img src="imgs/font_35_57_7/syn/35_57_7_17.svg">
	<img src="imgs/font_35_57_7/syn/35_57_7_00.svg">
	<img src="imgs/font_35_57_7/syn/35_57_7_15.svg"> 
	<img src="imgs/font_35_57_7/syn/35_57_7_07.svg">
	<img src="imgs/font_35_57_7/syn/35_57_7_21.svg"> 
	<img src="imgs/font_35_57_7/syn/35_57_7_30.svg"> 
	<img src="imgs/font_35_57_7/syn/35_57_7_28.svg"> 
	<img src="imgs/font_35_57_7/syn/35_57_7_05.svg"> 
	<img src="imgs/font_35_57_7/syn/35_57_7_40.svg">
	<img src="imgs/font_35_57_7/syn/35_57_7_39.svg"> 
	<img src="imgs/font_35_57_7/syn/35_57_7_45.svg"> 
	<br/>
	<img src="imgs/font_57/syn/57_18.svg"> 
	<img src="imgs/font_57/syn/57_08.svg"> 
	<img src="imgs/font_57/syn/57_06.svg"> 
	<img src="imgs/font_57/syn/57_06.svg">
	<img src="imgs/font_57/syn/57_17.svg">
	<img src="imgs/font_57/syn/57_00.svg">
	<img src="imgs/font_57/syn/57_15.svg"> 
	<img src="imgs/font_57/syn/57_07.svg"> 
	<img src="imgs/font_57/syn/57_21.svg"> 
	<img src="imgs/font_57/syn/57_30.svg"> 
	<img src="imgs/font_57/syn/57_28.svg"> 
	<img src="imgs/font_57/syn/57_05.svg"> 
	<img src="imgs/font_57/syn/57_40.svg">
	<img src="imgs/font_57/syn/57_39.svg"> 
	<img src="imgs/font_57/syn/57_45.svg"> 
	<br/>
</div>

### Random generation (New fonts)
Rendered:
<div align=center>
	<img src="imgs/font_18r_raw/syn/00.svg"> 
	<img src="imgs/font_18r_raw/syn/01.svg"> 
	<img src="imgs/font_18r_raw/syn/02.svg"> 
	<img src="imgs/font_18r_raw/syn/03.svg"> 
	<img src="imgs/font_18r_raw/syn/04.svg">
	<img src="imgs/font_18r_raw/syn/05.svg">
	<img src="imgs/font_18r_raw/syn/06.svg">
	<img src="imgs/font_18r_raw/syn/07.svg"> 
	<img src="imgs/font_18r_raw/syn/08.svg"> 
	<img src="imgs/font_18r_raw/syn/09.svg"> 
	<img src="imgs/font_18r_raw/syn/10.svg"> 
	<img src="imgs/font_18r_raw/syn/11.svg">
	<img src="imgs/font_18r_raw/syn/12.svg">
	<img src="imgs/font_18r_raw/syn/13.svg">
	<img src="imgs/font_18r_raw/syn/14.svg"> 
	<img src="imgs/font_18r_raw/syn/15.svg"> 
	<img src="imgs/font_18r_raw/syn/16.svg"> 
	<img src="imgs/font_18r_raw/syn/17.svg"> 
	<img src="imgs/font_18r_raw/syn/18.svg">
	<img src="imgs/font_18r_raw/syn/19.svg">
	<img src="imgs/font_18r_raw/syn/20.svg">
	<img src="imgs/font_18r_raw/syn/21.svg"> 
	<img src="imgs/font_18r_raw/syn/22.svg"> 
	<img src="imgs/font_18r_raw/syn/23.svg"> 	
	<img src="imgs/font_18r_raw/syn/24.svg">
	<img src="imgs/font_18r_raw/syn/25.svg">
	<br/>
	<img src="imgs/font_18r_raw/syn/26.svg"> 
	<img src="imgs/font_18r_raw/syn/27.svg"> 
	<img src="imgs/font_18r_raw/syn/28.svg"> 
	<img src="imgs/font_18r_raw/syn/29.svg"> 
	<img src="imgs/font_18r_raw/syn/30.svg">
	<img src="imgs/font_18r_raw/syn/31.svg">
	<img src="imgs/font_18r_raw/syn/32.svg">
	<img src="imgs/font_18r_raw/syn/33.svg"> 
	<img src="imgs/font_18r_raw/syn/34.svg"> 
	<img src="imgs/font_18r_raw/syn/35.svg"> 
	<img src="imgs/font_18r_raw/syn/36.svg"> 
	<img src="imgs/font_18r_raw/syn/37.svg">
	<img src="imgs/font_18r_raw/syn/38.svg">
	<img src="imgs/font_18r_raw/syn/39.svg">
	<img src="imgs/font_18r_raw/syn/40.svg"> 
	<img src="imgs/font_18r_raw/syn/41.svg"> 
	<img src="imgs/font_18r_raw/syn/42.svg"> 
	<img src="imgs/font_18r_raw/syn/43.svg"> 
	<img src="imgs/font_18r_raw/syn/44.svg">
	<img src="imgs/font_18r_raw/syn/45.svg">
	<img src="imgs/font_18r_raw/syn/46.svg">
	<img src="imgs/font_18r_raw/syn/47.svg"> 
	<img src="imgs/font_18r_raw/syn/48.svg"> 
	<img src="imgs/font_18r_raw/syn/49.svg">
	<img src="imgs/font_18r_raw/syn/50.svg">
	<img src="imgs/font_18r_raw/syn/51.svg">	
	<br/>
</div>

Outlines:
<div align=center>
	<img src="imgs/font_18r/syn/18r_00.svg"> 
	<img src="imgs/font_18r/syn/18r_01.svg"> 
	<img src="imgs/font_18r/syn/18r_02.svg"> 
	<img src="imgs/font_18r/syn/18r_03.svg"> 
	<img src="imgs/font_18r/syn/18r_04.svg">
	<img src="imgs/font_18r/syn/18r_05.svg">
	<img src="imgs/font_18r/syn/18r_06.svg">
	<img src="imgs/font_18r/syn/18r_07.svg"> 
	<img src="imgs/font_18r/syn/18r_08.svg"> 
	<img src="imgs/font_18r/syn/18r_09.svg"> 
	<img src="imgs/font_18r/syn/18r_10.svg"> 
	<img src="imgs/font_18r/syn/18r_11.svg">
	<img src="imgs/font_18r/syn/18r_12.svg">
	<img src="imgs/font_18r/syn/18r_13.svg">
	<img src="imgs/font_18r/syn/18r_14.svg"> 
	<img src="imgs/font_18r/syn/18r_15.svg"> 
	<img src="imgs/font_18r/syn/18r_16.svg"> 
	<img src="imgs/font_18r/syn/18r_17.svg"> 
	<img src="imgs/font_18r/syn/18r_18.svg">
	<img src="imgs/font_18r/syn/18r_19.svg">
	<img src="imgs/font_18r/syn/18r_20.svg">
	<img src="imgs/font_18r/syn/18r_21.svg"> 
	<img src="imgs/font_18r/syn/18r_22.svg"> 
	<img src="imgs/font_18r/syn/18r_23.svg"> 	
	<img src="imgs/font_18r/syn/18r_24.svg">
	<img src="imgs/font_18r/syn/18r_25.svg">
	<br/>
	<img src="imgs/font_18r/syn/18r_26.svg"> 
	<img src="imgs/font_18r/syn/18r_27.svg"> 
	<img src="imgs/font_18r/syn/18r_28.svg"> 
	<img src="imgs/font_18r/syn/18r_29.svg"> 
	<img src="imgs/font_18r/syn/18r_30.svg">
	<img src="imgs/font_18r/syn/18r_31.svg">
	<img src="imgs/font_18r/syn/18r_32.svg">
	<img src="imgs/font_18r/syn/18r_33.svg"> 
	<img src="imgs/font_18r/syn/18r_34.svg"> 
	<img src="imgs/font_18r/syn/18r_35.svg"> 
	<img src="imgs/font_18r/syn/18r_36.svg"> 
	<img src="imgs/font_18r/syn/18r_37.svg">
	<img src="imgs/font_18r/syn/18r_38.svg">
	<img src="imgs/font_18r/syn/18r_39.svg">
	<img src="imgs/font_18r/syn/18r_40.svg"> 
	<img src="imgs/font_18r/syn/18r_41.svg"> 
	<img src="imgs/font_18r/syn/18r_42.svg"> 
	<img src="imgs/font_18r/syn/18r_43.svg"> 
	<img src="imgs/font_18r/syn/18r_44.svg">
	<img src="imgs/font_18r/syn/18r_45.svg">
	<img src="imgs/font_18r/syn/18r_46.svg">
	<img src="imgs/font_18r/syn/18r_47.svg"> 
	<img src="imgs/font_18r/syn/18r_48.svg"> 
	<img src="imgs/font_18r/syn/18r_49.svg">
	<img src="imgs/font_18r/syn/18r_50.svg">
	<img src="imgs/font_18r/syn/18r_51.svg">	
	<br/>
</div>

## Citation:

If you use this code or find our work is helpful, please consider citing our work:
```
@inproceedings{wang2021deepvecfont,
 author = {Wang, Yizhi and Lian, Zhouhui},
 title = {DeepVecFont: Synthesizing High-quality Vector Fonts via Dual-modality Learning},
 journal = {ACM Transactions on Graphics},
 numpages = {15},
 volume={40},
 number={6},
 month = December,
 year = {2021},
 doi={10.1145/3478513.3480488}
}
```
