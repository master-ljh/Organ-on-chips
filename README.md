# Organ-on-chips
## daily_note
2023-2-27 :
    
    1. 之前的思路是错误的，今天重新整理了思路。分别对肿瘤数据进行分割标注，对血管数据进行检测标注。完成检测器和分割的训练之后。直接加入追踪器。
    
    2.目前进展：
        使用yolo推荐的标注工具，对肿瘤数据进行分割标注。

    3.大论文：
        先写综述部分。综述部分的思路如下:
            1.器官芯片的发展很不错，对世界带来了改变 
            2.器官芯片和人工智能结合的领域，举例说明，有哪些
            3.目标追踪技术在器官芯片领域的应用几乎是空白的，本文找了两个切入点：（1）血管类器官（2）肿瘤扩散
            4.目标追踪技术是多阶段任务，必须要检测 -> 追踪；分割 -> 追踪

2023-2-28:

    1.肿瘤分割数据标注完成
    2.肿瘤分割数据集创建完成
    3.构建好的数据集送入网络训练
    4.对四个方向  
        a.器官芯片的综述
        b.目标追踪的综述 -> 两阶段训练，目标检测/目标分割 -> 目标追踪
            （1）.目标检测的综述
            （2）.目标分割的综述
    summary：1.2两个任务完成，3.4 留到3.1号做

2023-3-1：

    1.将肿瘤分割数据集送入网络训练，等待训练结果
    2.列出论文大纲，并跟陈老师讨论
    3.开始写综述：
        对四个方向  
        1.器官芯片的综述
        2.目标追踪的综述 -> 两阶段训练，目标检测/目标分割 -> 目标追踪
            （1）.目标检测的综述
            （2）.目标分割的综述
    4.血管类器官的数据，今天下午五点出来结果
        a.对数据进行标注
        b.创建数据集
        c.血管类器官的数据集送入网络

2023-3-2:
   
    1.肿瘤分割数据训练结果不理想，准备尝试yolov8x-seg训练。
    2.跟陈老师汇报一下进程，就开始写论文
    3.王妍师姐今天能把数据给我的话，我就可以今天开始标注。白细胞追踪也可以得到结果。