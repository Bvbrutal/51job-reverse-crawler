from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from PIL import Image

# 初始化
# 防止打印一些无用的日志
option = webdriver.ChromeOptions()
option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
web = Chrome(options=option)
# 设置等待超时
wait = WebDriverWait(web, 100)


# 登录
def login(url):
    web.get(url)
    web.maximize_window()  # 窗口最大化
    time.sleep(2)
    # 登录
    web.find_element(By.ID, 'loginname').send_keys('18875370169')
    web.find_element(By.ID, 'password').send_keys('zxcvbnm123')
    web.find_element(By.ID, 'isread_em').click()
    time.sleep(0.2)
    web.find_element(By.ID, 'login_btn_withPwd').click()
    time.sleep(1)


# 对某元素截图
def save_pic(obj, name):
    try:
        time.sleep(1)
        pic_url = web.save_screenshot(f'static/img/51job{name}.png')
        print("%s:截图成功!" % pic_url)

        # 获取元素位置信息//是否乘1.25与电脑屏幕分辨率有关。
        left = obj.location['x']*1.25  # 自己通过原图与实际图片对比得出的系数
        top = obj.location['y']*1.25
        right = left + obj.size['width']*1.25
        bottom = top + obj.size['height']*1.25

        print('图：' + name)
        print('Left %s' % left)
        print('Top %s' % top)
        print('Right %s' % right)
        print('Bottom %s' % bottom)
        print('')

        im = Image.open(f'static/img/51job{name}.png')
        im = im.crop((left, top, right, bottom))  # 元素裁剪
        file_name = 'static/img/51job_' + name + '.png'
        im.save(file_name)  # 元素截图
    except BaseException as msg:
        print("%s:截图失败!" % msg)


# 设置元素可见
def show_element(element):
    web.execute_script("arguments[0].style=arguments[1]", element, "display: block;")


# 设置元素不可见
def hide_element(element):
    web.execute_script("arguments[0].style=arguments[1]", element, "display: none;")


def cut():
    c_background = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'canvas.geetest_canvas_bg.geetest_absolute')))
    c_slice = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'canvas.geetest_canvas_slice.geetest_absolute')))
    c_full_bg = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'canvas.geetest_canvas_fullbg.geetest_fade.geetest_absolute')))
    hide_element(c_slice)
    save_pic(c_background, 'back')  # 隐藏滑块
    show_element(c_slice)
    save_pic(c_slice, 'slice')  # 所有的
    show_element(c_full_bg)
    save_pic(c_full_bg, 'full')  # 隐藏所有的


# 判断像素是否相同
def is_pixel_equal(bg_image, fullbg_image, x, y):
    """
    :param bg_image: (Image)缺口图片
    :param fullbg_image: (Image)完整图片
    :param x: (Int)位置x
    :param y: (Int)位置y
    :return: (Boolean)像素是否相同
    """
    # 获取缺口图片的像素点(按照RGB格式)
    bg_pixel = bg_image.load()[x, y]
    # 获取完整图片的像素点(按照RGB格式)
    fullbg_pixel = fullbg_image.load()[x, y]
    # 设置一个判定值，像素值之差超过判定值则认为该像素不相同
    threshold = 50
    # 判断像素的各个颜色之差，abs()用于取绝对值
    if (abs(bg_pixel[0] - fullbg_pixel[0] < threshold) and abs(bg_pixel[1] - fullbg_pixel[1] < threshold) and abs(
            bg_pixel[2] - fullbg_pixel[2] < threshold)):
        # 如果差值在判断值之内，返回是相同像素
        return True
    else:
        # 如果差值在判断值之外，返回不是相同像素
        return False


# 计算滑块移动距离
def get_distance(bg_image, fullbg_image):
    '''
    :param bg_image: (Image)缺口图片
    :param fullbg_image: (Image)完整图片
    :return: (Int)缺口离滑块的距离
    '''
    # 滑块的初始位置
    distance = 40
    # 遍历像素点横坐标
    print('fullbg_image:')
    print(fullbg_image.size[0])
    print(fullbg_image.size[1])

    for i in range(distance, fullbg_image.size[0]):
        # 遍历像素点纵坐标
        for j in range(fullbg_image.size[1]):
            # 如果不是相同像素
            if not is_pixel_equal(fullbg_image, bg_image, i, j):
                # 返回此时横轴坐标就是滑块需要移动的距离
                print(i)
                return i/1.25


# 破解滑块验证
def slide():
    distance = get_distance(Image.open('static/img/51job_back.png'), Image.open('static/img/51job_full.png'))-5  # 要将原图与实际图对比的系数除掉
    try:
        slider = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.geetest_slider_button')))  # 找到滑块
        if slider:
            print("====有滑块验证=====")
            action_chains = webdriver.ActionChains(web)
            # 点击，准备拖拽
            action_chains.click_and_hold(slider)
            action_chains.pause(0.2)
            action_chains.move_by_offset(distance-10, 0)
            action_chains.pause(0.6)
            action_chains.move_by_offset(10, 0)  # 添加修正过程
            action_chains.pause(0.6)
            action_chains.release()
            action_chains.perform()  # 释放滑块
            time.sleep(5)
        else:
            print("===没有滑块验证===")
    except Exception as e:
        print("===" + str(e))

def loin():
    url = 'https://login.51job.com/login.php?loginway=0&isjump=0&lang=c&from_domain=i&url=http%3A%2F%2Fwww.51job.com%2F'
    login(url)
    cut()
    slide()
    web.close()

if __name__ == '__main__':
    loin()