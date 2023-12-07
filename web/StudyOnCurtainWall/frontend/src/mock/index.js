import Mock from 'mockjs'

// 是否使用mock.js模拟数据
// let useMock = true
let useMock = true;
if (useMock) {
   
    //获得石材幕墙局部图像的裂痕识别结果数据
    //这里说的“石材幕墙局部图像的裂痕识别结果数据”，是指对于整张局部图像识别的统计结果
    Mock.mock(/api\/StoneCrackDetect\/data\?image_name=(.*)/ , 'get',
    function(options){
      // 从 URL 中获取 image_name
      let imageName = options.url.match(/image_name=(.*)/)[1];
      // 拼接字符串
      let imagePath = '/DZGCG/Pictures/' + imageName;
      // 返回结果
      return {
          image_path: imagePath,
          image_width: 0,
          image_height: 0,
          has_crack: true,
          crack_data: {
            crack_pixel_area: 1,
            crack_physical_area: 2,
            crack_pixel_length: 3,
            crack_physical_length: 4,
            crack_pixel_average_width: 5,
            crack_physical_average_width: 6,
            crack_pixel_max_width: 7,
            crack_physical_max_width: 8
        }
    }
  });


    //获取幕墙局部图像中幕墙块的识别结果集合
    //根据图像分割的结果，返回图像分割与识别的中间图片路径，和每张幕墙块图像的识别结果数据
    Mock.mock(/api\/StoneCrackDetect\/block_data\?image_name=.*/, 'get', {
        seg_process_image_path: "/DZGCG/seg/mask.png",
        seg_count: 7,
        block_data: [
          {
            block_num: 1,
            block_seg_image_path: "/DZGCG/seg/img1.png",
            block_detect_image_path: "/DZGCG/result/img1.png",
            image_width: 0,
            image_height: 0,
            has_crack: true,
            crack_data: {
              crack_pixel_area: 1,
              crack_physical_area: 2,
              crack_pixel_length: 3,
              crack_physical_length: 4,
              crack_pixel_average_width: 5,
              crack_physical_average_width: 6,
              crack_pixel_max_width: 7,
              crack_physical_max_width: 8
            }
          },
          {
            block_num: 2,
            block_seg_image_path: "/DZGCG/seg/img2.png",
            block_detect_image_path: "/DZGCG/result/img2.png",
            image_width: 0,
            image_height: 0,
            has_crack: true,
            crack_data: {
              crack_pixel_area: 1,
              crack_physical_area: 2,
              crack_pixel_length: 3,
              crack_physical_length: 4,
              crack_pixel_average_width: 5,
              crack_physical_average_width: 6,
              crack_pixel_max_width: 7,
              crack_physical_max_width: 8
            }
          },
          {
            block_num: 3,
            block_seg_image_path: "/DZGCG/seg/img3.png",
            block_detect_image_path: "/DZGCG/result/img3.png",
            image_width: 0,
            image_height: 0,
            has_crack: true,
            crack_data: {
              crack_pixel_area: 1,
              crack_physical_area: 2,
              crack_pixel_length: 3,
              crack_physical_length: 4,
              crack_pixel_average_width: 5,
              crack_physical_average_width: 6,
              crack_pixel_max_width: 7,
              crack_physical_max_width: 8
            }
          },
          {
            block_num: 4,
            block_seg_image_path: "/DZGCG/seg/img4.png",
            block_detect_image_path: "/DZGCG/result/img4.png",
            image_width: 0,
            image_height: 0,
            has_crack: true,
            crack_data: {
              crack_pixel_area: 1,
              crack_physical_area: 2,
              crack_pixel_length: 3,
              crack_physical_length: 4,
              crack_pixel_average_width: 5,
              crack_physical_average_width: 6,
              crack_pixel_max_width: 7,
              crack_physical_max_width: 8
            }
          },
          {
            block_num: 5,
            block_seg_image_path: "/DZGCG/seg/img5.png",
            block_detect_image_path: "/DZGCG/result/img5.png",
            image_width: 0,
            image_height: 0,
            has_crack: true,
            crack_data: {
              crack_pixel_area: 1,
              crack_physical_area: 2,
              crack_pixel_length: 3,
              crack_physical_length: 4,
              crack_pixel_average_width: 5,
              crack_physical_average_width: 6,
              crack_pixel_max_width: 7,
              crack_physical_max_width: 8
            }
          },
          {
            block_num: 10,
            block_seg_image_path: "/DZGCG/seg/img10.png",
            block_detect_image_path: "/DZGCG/result/img10.png",
            image_width: 0,
            image_height: 0,
            has_crack: true,
            crack_data: {
              crack_pixel_area: 1,
              crack_physical_area: 2,
              crack_pixel_length: 3,
              crack_physical_length: 4,
              crack_pixel_average_width: 5,
              crack_physical_average_width: 6,
              crack_pixel_max_width: 7,
              crack_physical_max_width: 8
            }
          },
          {
            block_num: 13,
            block_seg_image_path: "/DZGCG/seg/img13.png",
            block_detect_image_path: "/DZGCG/result/img13.png",
            image_width: 0,
            image_height: 0,
            has_crack: true,
            crack_data: {
              crack_pixel_area: 1,
              crack_physical_area: 2,
              crack_pixel_length: 3,
              crack_physical_length: 4,
              crack_pixel_average_width: 5,
              crack_physical_average_width: 6,
              crack_pixel_max_width: 7,
              crack_physical_max_width: 8
            }
          },
        ]
    })

}

export default Mock