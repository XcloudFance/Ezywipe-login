这里是 Ezywipe 官网 的简略开发者文档

1.目录介绍
—— static
———— assets 存放部分css/js
———— css,js 存放部分css/js
———— images 存放官网部分素材
—————— 相对应的图片可以在官网看，必要维护的时候将图片覆盖到对应名字即可修改
———— video 里面就放了一个介绍.mp4 需要修改mp4时直接覆盖
———— webfonts 里面的字体并不是真正的使用，只是部分素材需要用到，且皆为开源字体，为保险起见就将字体99%的修改成了Hansans(思源黑体)
———— image_ezywipe 还是部分素材
———— image_retail 存放retail页面的素材
—————— imageretail下的素材假设有5种:
1[0].jpg 1[1].jpg 1[2].jpg 1[3].jpg 1[4].jpg 1[5].jpg……以此类推
每个jpg的[0]就是首页，并且按顺序是进去详情页面的顺序，无论产品有多少张都只能放6张，不能多也不能少，想修改必须从python代码和html代码里同时修改


2.数据库操作