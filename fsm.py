from transitions.extensions import GraphMachine
from PIL import Image
import re

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )
    def is_going_to_state0(self, update):
        text = update.message.text
       	return text.lower() == 'hi'
    def is_going_to_state1(self, update):
        text = update.message.text
        return text.lower() == '想'
     
##########################################################################         
    def is_going_to_state2(self, update):
        text = update.message.text
        return text.lower() == '北部'
         
    def is_going_to_state3(self, update):
        text = update.message.text
        return text.lower() == '中部'
         
    def is_going_to_state4(self, update):
        text = update.message.text
        return text.lower() == '南部'
         
    def is_going_to_state5(self, update):
        text = update.message.text
        return text.lower() == '東部'
############################################################################    
    def is_going_to_state6(self, update):
       	text = update.message.text
       	return text.lower() == '台北市'
    def is_going_to_state7(self, update):
        text = update.message.text
        return text.lower() == '新北市'
    def is_going_to_state8(self, update):
        text = update.message.text
        return text.lower() == '基隆市'
    def is_going_to_state9(self, update):
        text = update.message.text
        return text.lower() == '桃園縣'
    def is_going_to_state10(self, update):
        text = update.message.text
        return text.lower() == '新竹縣'
    def is_going_to_state11(self, update):
        text = update.message.text
        return text.lower() == '新竹市'
    def is_going_to_state12(self, update):
        text = update.message.text
        return text.lower() == '宜蘭縣'

#############################################################################
    def is_going_to_state13(self, update):
        text = update.message.text
        return text.lower() == '苗栗縣'
    def is_going_to_state14(self, update):
        text = update.message.text
        return text.lower() == '台中市'
    def is_going_to_state15(self, update):
        text = update.message.text
        return text.lower() == '彰化縣'
    def is_going_to_state16(self, update):
        text = update.message.text
        return text.lower() == '雲林縣'
    def is_going_to_state17(self, update):
        text = update.message.text
        return text.lower() == '南投縣'
    
#############################################################################
    def is_going_to_state18(self, update):
        text = update.message.text
        return text.lower() == '嘉義縣'
    def is_going_to_state19(self, update):
        text = update.message.text
        return text.lower() == '嘉義市'
    def is_going_to_state20(self, update):
        text = update.message.text
        return text.lower() == '台南市'
    def is_going_to_state21(self, update):
        text = update.message.text
        return text.lower() == '高雄市'
    def is_going_to_state22(self, update):
        text = update.message.text
        return text.lower() == '屏東縣'

#############################################################################
    def is_going_to_state23(self, update):
        text = update.message.text
        return text.lower() == '花蓮縣'
    def is_going_to_state24(self, update):
        text = update.message.text
        return text.lower() == '台東縣'

#############################################################################
    def is_going_to_state25(self, update):
        text = update.message.text
        return text.lower() == '1'
    def is_going_to_state26(self, update):
        text = update.message.text
        return text.lower() == '2'  

#############################################################################    
    def is_going_to_state27(self, update):
        text = update.message.text
        return text.lower() == '1'
    def is_going_to_state28(self, update):
        text = update.message.text
        return text.lower() == '2'

############################################################################# 
    def is_going_to_state29(self, update):
        text = update.message.text
        return text.lower() == '1'
    def is_going_to_state30(self, update):
        text = update.message.text
        return text.lower() == '2'

############################################################################# 
    def is_going_to_state31(self, update):
        text = update.message.text
        return text.lower() == '1'
    def is_going_to_state32(self, update):
        text = update.message.text
        return text.lower() == '2'

############################################################################# 
    def is_going_to_state33(self, update):
        text = update.message.text
        return text.lower() == '1'
    def is_going_to_state34(self, update):
        text = update.message.text
        return text.lower() == '2'

############################################################################# 
    def is_going_to_state35(self, update):
        text = update.message.text
        return text.lower() == '1'
    def is_going_to_state36(self, update):
        text = update.message.text
        return text.lower() == '2'

############################################################################# 
    def is_going_to_state37(self, update):
        text = update.message.text
        return text.lower() == '1'
    def is_going_to_state38(self, update):
        text = update.message.text
        return text.lower() == '2'
#############################################################################
    def is_going_to_state39(self, update):
        text = update.message.text
        return text.lower() == '1'
    def is_going_to_state40(self, update):
        text = update.message.text
        return text.lower() == '2'
    def is_going_to_state41(self, update):
        text = update.message.text
        return text.lower() == '3'

############################################################################# 
    def is_going_to_state42(self, update):
        text = update.message.text
        return text.lower() == '1'
    def is_going_to_state43(self, update):
        text = update.message.text
        return text.lower() == '2'
    def is_going_to_state44(self, update):
        text = update.message.text
        return text.lower() == '3'

############################################################################# 
    def is_going_to_state45(self, update):
        text = update.message.text
        return text.lower() == '1'

#############################################################################
    def is_going_to_state46(self, update):
        text = update.message.text
        return text.lower() == '1'
    def is_going_to_state47(self, update):
        text = update.message.text
        return text.lower() == '2'
    def is_going_to_state48(self, update):
        text = update.message.text
        return text.lower() == '3'

############################################################################# 
    def is_going_to_state49(self, update):
        text = update.message.text
        return text.lower() == '1'
    def is_going_to_state50(self, update):
        text = update.message.text
        return text.lower() == '2'
    def is_going_to_state51(self, update):
        text = update.message.text
        return text.lower() == '3'

############################################################################# 
    def is_going_to_state52(self, update):
        text = update.message.text
        return text.lower() == '1'
    def is_going_to_state53(self, update):
        text = update.message.text
        return text.lower() == '2'
    def is_going_to_state54(self, update):
        text = update.message.text
        return text.lower() == '3'

############################################################################# 
    def is_going_to_state55(self, update):
        text = update.message.text
        return text.lower() == '1'
    def is_going_to_state56(self, update):
        text = update.message.text
        return text.lower() == '2'
    def is_going_to_state57(self, update):
        text = update.message.text
        return text.lower() == '3'

#############################################################################
    def is_going_to_state58(self, update):
        text = update.message.text
        return text.lower() == '1'
    def is_going_to_state59(self, update):
        text = update.message.text
        return text.lower() == '2'
	 
############################################################################# 
    def is_going_to_state60(self, update):
        text = update.message.text
        return text.lower() == '1'
    def is_going_to_state61(self, update):
        text = update.message.text
        return text.lower() == '2'

############################################################################# 
    def is_going_to_state62(self, update):
        text = update.message.text
        return text.lower() == '1'
    def is_going_to_state63(self, update):
        text = update.message.text
        return text.lower() == '2'

############################################################################# 
    def is_going_to_state64(self, update):
        text = update.message.text
        return text.lower() == '1'
    def is_going_to_state65(self, update):
        text = update.message.text
        return text.lower() == '2'

############################################################################# 
    def is_going_to_state66(self, update):
        text = update.message.text
        return text.lower() == '1'
    def is_going_to_state67(self, update):
        text = update.message.text
        return text.lower() == '2'

############################################################################# 
    def is_going_to_state68(self, update):
        text = update.message.text
        return text.lower() == '1'
    def is_going_to_state69(self, update):
        text = update.message.text
        return text.lower() == '2'
    def is_going_to_state70(self, update):
        text = update.message.text
        return text.lower() == '3'

############################################################################# 
    def is_going_to_state71(self, update):
        text = update.message.text
        return text.lower() == '1'
    def is_going_to_state72(self, update):
        text = update.message.text
        return text.lower() == '2'
    def is_going_to_state73(self, update):
        text = update.message.text
        return text.lower() == '3'

############################################################################# 
    def is_going_to_state74(self, update):
        text = update.message.text
        return text.lower() == '1'
    def is_going_to_state75(self, update):
        text = update.message.text
        return text.lower() == '2'
    def is_going_to_state76(self, update):
        text = update.message.text
        return text.lower() == '3'

############################################################################# 
    def is_going_to_state77(self, update):
        text = update.message.text
        return text.lower() == '1'
    def is_going_to_state78(self, update):
        text = update.message.text
        return text.lower() == '2'
    def is_going_to_state79(self, update):
        text = update.message.text
        return text.lower() == '3'

############################################################################# 
    def is_going_to_state80(self, update):
        text = update.message.text
        return text.lower() == '1'
    def is_going_to_state81(self, update):
        text = update.message.text
        return text.lower() == '2'
    def is_going_to_state82(self, update):
        text = update.message.text
        return text.lower() == '3'

############################################################################# 
    def is_going_to_state83(self, update):
        text = update.message.text
        return text.lower() == '1'
    def is_going_to_state84(self, update):
        text = update.message.text
        return text.lower() == '2'

#############################################################################
    def is_going_to_state85(self, update):
        text = update.message.text
        return text.lower() == '1'
    def is_going_to_state86(self, update):
        text = update.message.text
        return text.lower() == '2'

#############################################################################
    def is_going_to_state87(self, update):
        text = update.message.text
        return text.lower() == '1'
    def is_going_to_state88(self, update):
        text = update.message.text
        return text.lower() == '2'

#############################################################################
    def is_going_to_state89(self, update):
        text = update.message.text
        return text.lower() == '1'
    def is_going_to_state90(self, update):
        text = update.message.text
        return text.lower() == '2'

#############################################################################
    def is_going_to_state91(self, update):
        text = update.message.text
        return text.lower() == '1'
    def is_going_to_state92(self, update):
        text = update.message.text
        return text.lower() == '2'

#############################################################################
    def is_going_to_state93(self, update):
        text = update.message.text
        return text.lower() == '1'
    def is_going_to_state94(self, update):
        text = update.message.text
        return text.lower() == '2'
    def is_going_to_state95(self, update):
        text = update.message.text
        return text.lower() == '3'

#############################################################################
    def is_going_to_state96(self, update):
        text = update.message.text
        return text.lower() == '1'
    def is_going_to_state97(self, update):
        text = update.message.text
        return text.lower() == '2'
    def is_going_to_state98(self, update):
        text = update.message.text
        return text.lower() == '3'

#############################################################################
    def is_going_to_state99(self, update):
        text = update.message.text
        return text.lower() == '1'
    def is_going_to_state100(self, update):
        text = update.message.text
        return text.lower() == '2'
    def is_going_to_state101(self, update):
        text = update.message.text
        return text.lower() == '3'

#############################################################################
    def is_going_to_state102(self, update):
        text = update.message.text
        return text.lower() == '1'
    def is_going_to_state103(self, update):
        text = update.message.text
        return text.lower() == '2'
    def is_going_to_state104(self, update):
        text = update.message.text
        return text.lower() == '3'

#############################################################################
    def is_going_to_state105(self, update):
        text = update.message.text
        return text.lower() == '1'
    def is_going_to_state106(self, update):
        text = update.message.text
        return text.lower() == '2'
    def is_going_to_state107(self, update):
        text = update.message.text
        return text.lower() == '3'

#############################################################################
    def is_going_to_state108(self, update):
        text = update.message.text
        return text.lower() == '1'
    def is_going_to_state109(self, update):
        text = update.message.text
        return text.lower() == '2'

#############################################################################
    def is_going_to_state110(self, update):
        text = update.message.text
        return text.lower() == '1'
    def is_going_to_state111(self, update):
        text = update.message.text
        return text.lower() == '2'

#############################################################################
    def is_going_to_state112(self, update):
        text = update.message.text
        return text.lower() == '1'
    def is_going_to_state113(self, update):
        text = update.message.text
        return text.lower() == '2'
    def is_going_to_state114(self, update):
        text = update.message.text
        return text.lower() == '3'

#############################################################################
    def is_going_to_state115(self, update):
        text = update.message.text
        return text.lower() == '1'
    def is_going_to_state116(self, update):
        text = update.message.text
        return text.lower() == '2'
    def is_going_to_state117(self, update):
        text = update.message.text
        return text.lower() == '3'

#############################################################################

    def on_enter_state0(self, update):
        update.message.reply_text("想不想要知道我私房的景點？")
        #self.go_back(update)

    def on_enter_state1(self, update):
        update.message.reply_text("要北部、中部、南部還是東部？")
        #self.go_back(update)
     
############################################################################
    def on_enter_state2(self, update): #####北
        update.message.reply_text("哪個縣市呢？")
    def on_enter_state3(self, update): #####中
        update.message.reply_text("哪個縣市呢？")
    def on_enter_state4(self, update): #####南
        update.message.reply_text("哪個縣市呢？")
    def on_enter_state5(self, update): #####東
        update.message.reply_text("哪個縣市呢？")
 
############################################################################
    def on_enter_state6(self, update):
        update.message.reply_text("想要我推薦請輸入：1\n繼續查詢請輸入：2")
    def on_enter_state7(self, update):     	        
       	update.message.reply_text("想要我推薦請輸入：1\n繼續查詢請輸入：2")
    def on_enter_state8(self, update):                 
       	update.message.reply_text("想要我推薦請輸入：1\n繼續查詢請輸入：2")
    def on_enter_state9(self, update):
        update.message.reply_text("想要我推薦請輸入：1\n繼續查詢請輸入：2")
    def on_enter_state10(self, update):
        update.message.reply_text("想要我推薦請輸入：1\n繼續查詢請輸入：2")
    def on_enter_state11(self, update): 
        update.message.reply_text("想要我推薦請輸入：1\n繼續查詢請輸入：2")
    def on_enter_state12(self, update):
        update.message.reply_text("想要我推薦請輸入：1\n繼續查詢請輸入：2")

############################################################################
    def on_enter_state13(self, update):
        update.message.reply_text("想要我推薦請輸入：1\n繼續查詢請輸入：2")
    def on_enter_state14(self, update):
        update.message.reply_text("想要我推薦請輸入：1\n繼續查詢請輸入：2")    
    def on_enter_state15(self, update):
        update.message.reply_text("想要我推薦請輸入：1\n繼續查詢請輸入：2")
    def on_enter_state16(self, update):
        update.message.reply_text("想要我推薦請輸入：1\n繼續查詢請輸入：2")
    def on_enter_state17(self, update):
        update.message.reply_text("想要我推薦請輸入：1\n繼續查詢請輸入：2")  
########################################################################   
    def on_enter_state18(self, update): 
        update.message.reply_text("想要我推薦請輸入：1\n繼續查詢請輸入：2")
    def on_enter_state19(self, update):
        update.message.reply_text("想要我推薦請輸入：1\n繼續查詢請輸入：2")
    def on_enter_state20(self, update):
        update.message.reply_text("想要我推薦請輸入：1\n繼續查詢請輸入：2")
    def on_enter_state21(self, update):
        update.message.reply_text("想要我推薦請輸入：1\n繼續查詢請輸入：2")
    def on_enter_state22(self, update):
        update.message.reply_text("想要我推薦請輸入：1\n繼續查詢請輸入：2")

############################################################################
    def on_enter_state23(self, update):
        update.message.reply_text("想要我推薦請輸入：1\n繼續查詢請輸入：2")
    def on_enter_state24(self, update):
        update.message.reply_text("想要我推薦請輸入：1\n繼續查詢請輸入：2")
  
############################################################################
    def on_enter_state25(self, update):
       	update.message.reply_text("我推薦這個網址看看吧\nhttps://asiayo.com/event/taipei_fit.html?utm_source=google_adwords&utm_campaign=41559906396&utm_medium=cpc&utm_term=%E5%8F%B0%E5%8C%97%E6%99%AF%E9%BB%9E&gclid=CjsKDwjw6qnJBRDpoonDwLSeZhIkAIpTR8Iyi3nyYXkAif-Q7c3M0E7UHrsjmDttQbkeZ-ck92p_GgKg-fD_BwE\n")
       	update.message.reply_text("http://www.liviatravel.com/2011/10/blog-post_8963.html")
       	self.go_back(update)
    def on_enter_state26(self, update):
        update.message.reply_text("想要哪種種類呢？\n")
       	update.message.reply_text("1.人文\n")
       	photo=open('pic/1.jpg','rb')
       	update.message.reply_photo(photo)
       	photo.close()
       	update.message.reply_text("2.自然\n")
        photo=open('pic/2.jpg','rb')
        update.message.reply_photo(photo)
       	photo.close()
        update.message.reply_text("3.親子共遊\n")
        photo=open('pic/3.jpg','rb')
        update.message.reply_photo(photo)
       	photo.close()
###########################################################################
    def on_enter_state27(self, update):
        update.message.reply_text("我推薦這個網址看看吧\nhttp://nixojov.pixnet.net/blog/post/339225569-%E6%96%B0%E5%8C%97%E5%B8%82%E5%A5%BD%E7%8E%A9%E7%9A%84%E5%9C%A8%E5%9C%B0%E6%8E%A8%E8%96%A6%E6%97%85%E9%81%8A%E6%99%AF%E9%BB%9E%E3%80%81%E8%A7%80%E5%85%89%E6%99%AF%E9%BB%9E%E3%80%81\n")
        update.message.reply_text("http://blog.xuite.net/bobowin/me/67990671-%5B+%E6%96%B0%E5%8C%97%E5%B8%82%E4%B8%80%E6%97%A5%E9%81%8A%5D+%E5%A5%BD%E5%90%83%E5%A5%BD%E7%8E%A9%2F%E6%99%AF%E8%A7%80%E9%A4%90%E5%BB%B3%2F%E4%B8%80%E6%97%A5%E9%81%8A%2F%E4%BA%8C%E6%97%A5%E9%81%8A%2F%E6%99%AF%E8%A7%80%E9%A4%90%E5%BB%B3%2F%E8%A1%8C%E7%A8%8B%E8%A6%8F%E5%8A%83")
        self.go_back(update)
    def on_enter_state28(self, update):
        update.message.reply_text("想要哪種種類呢？")
        update.message.reply_text("1.人文\n")
        photo=open('pic/13.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("2.自然\n")
        photo=open('pic/14.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("3.親子共遊\n")
        photo=open('pic/15.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
  
############################################################################
    def on_enter_state29(self, update):
        update.message.reply_text("我推薦這個網址看看吧\nhttps://www.tripadvisor.com.tw/Attractions-g317130-Activities-Keelung.html\n")
        update.message.reply_text("http://blog.xuite.net/bobowin/me/63522707")
        self.go_back(update)
    def on_enter_state30(self, update):
        update.message.reply_text("想要哪種種類呢？")
        update.message.reply_text("1.自然\n")
        photo=open('pic/25.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()	

############################################################################
    def on_enter_state31(self, update):
        update.message.reply_text("我推薦這個網址看看吧\nhttp://s045488.pixnet.net/blog/post/73559770-%E3%80%8A%E6%A1%83%E5%9C%92%E6%99%AF%E9%BB%9E%E3%80%8B%E6%A1%83%E5%9C%92%E4%B8%80%E6%97%A5%E9%81%8A%E6%8E%A8%E8%96%A6%E2%95%91%E6%A1%83%E5%9C%92%E6%99%AF%E8%A7%80%E9%A4%90%E5%BB%B3\n")
        update.message.reply_text("http://yoke918.com/?cat=49")
        self.go_back(update)
    def on_enter_state32(self, update):
        update.message.reply_text("想要哪種種類呢？")
        update.message.reply_text("1.人文\n")
        photo=open('pic/29.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("2.自然\n")
        photo=open('pic/30.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("3.親子共遊\n")
        photo=open('pic/31.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
  
############################################################################
    def on_enter_state33(self, update):
        update.message.reply_text("我推薦這個網址看看吧\nhttp://bob20842.pixnet.net/blog/post/368496105-%E6%96%B0%E7%AB%B9%E6%97%85%E9%81%8A%E6%99%AF%E9%BB%9E%2A34%E6%87%B6%E4%BA%BA%E5%8C%85%28%E8%A7%80%E9%9C%A7%E9%9B%AA%E9%9C%B8-%E5%8C%97%E5%9F%94%E8%80%81%E8%A1%97-%E5%8F%B8\n")
        update.message.reply_text("http://yoke918.com/?tag=%E6%96%B0%E7%AB%B9%E6%97%85%E9%81%8A%E6%99%AF%E9%BB%9E")
        self.go_back(update)
    def on_enter_state34(self, update):
        update.message.reply_text("想要哪種種類呢？")
        update.message.reply_text("1.人文\n")
        photo=open('pic/33.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("2.自然\n")
        photo=open('pic/32.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("3.親子共遊\n")
        photo=open('pic/34.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()

  
############################################################################
    def on_enter_state35(self, update):
        update.message.reply_text("我推薦這個網址看看吧\nhttp://chibli.pixnet.net/blog/post/65588446-%5B%E9%81%8A%E3%80%82%E6%96%B0%E7%AB%B9%5D-%E6%96%B0%E7%AB%B9%E8%A7%80%E5%85%89%E3%80%81%E6%97%85%E9%81%8A%E6%99%AF%E9%BB%9E-\n")
        update.message.reply_text("https://www.tripadvisor.com.tw/Attractions-g297906-Activities-Hsinchu.html")
        self.go_back(update)
    def on_enter_state36(self, update):
        update.message.reply_text("想要哪種種類呢？")
        update.message.reply_text("1.人文\n")
        photo=open('pic/35.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("2.自然\n")
        photo=open('pic/36.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("3.親子共遊\n")
        photo=open('pic/37.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
  
############################################################################
    def on_enter_state37(self, update):
        update.message.reply_text("我推薦這個網址看看吧\nhttp://lolwarden.pixnet.net/blog/post/189377245-2017%E5%AE%9C%E8%98%AD%E8%A1%8C%E7%A8%8B%E8%B7%AF%E7%B7%9A%E8%A6%8F%E5%8A%83%EF%BC%8C%E4%B8%80%E6%97%A5%E9%81%8A%E3%80%81%E4%BA%8C%E6%97%A5%E9%81%8A%E6%97%85%E9%81%8A\n")
        update.message.reply_text("http://rechal63.pixnet.net/blog/post/59152447-%E3%80%90%E5%AE%9C%E8%98%AD%E5%86%AC%E5%AD%A3%E7%89%B9%E8%BC%AF%E3%80%91%E5%AE%9C%E8%98%AD42%E5%80%8B%E9%9B%A8%E5%A4%A9%E5%82%99%E6%A1%88%E6%99%AF%E9%BB%9E%EF%BC%8B%E5%90%83")
        self.go_back(update)
    def on_enter_state38(self, update):
        update.message.reply_text("想要哪種種類呢？")
        update.message.reply_text("1.人文\n")
        photo=open('pic/38.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("2.自然\n")
        photo=open('pic/39.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("3.親子共遊\n")
        photo=open('pic/40.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
  
#############################################################################
    def on_enter_state39(self, update):
        update.message.reply_text("查詢的結果：\n")
        photo=open('pic/4.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：松山文創園區\n地址：臺北市信義區光復南路133號\n網路資訊：http://www.songshanculturalpark.org/\n")
        photo=open('pic/5.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：二二和平公園\n地址：臺北市中正區懷寧街、襄陽路、公園路、凱達>格蘭大道口\n網路資訊：http://228memorialmuseum.gov.taipei/ct.asp?xItem=1874245&ctNode=38980&mp=11900A\n")
        photo=open('pic/6.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：兩廳院\n地址：臺北市中正區中山南路21-1號\n網路資訊：http://npac-ntch.org/index.html\n")
        update.message.reply_text("想要更多旅遊地點,可以參考此網站：https://www.travel.taipei/zh-tw\n")
        self.go_back(update)
    def on_enter_state40(self, update):
        update.message.reply_text("查詢的結果：\n")
        photo=open('pic/7.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：關渡自然公園\n地址：臺北市北投區關渡路55號\n網路資訊：http://gd-park.org.tw/\n")
        photo=open('pic/8.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：芝山文化生態綠園\n地址：臺北市士林區雨聲街120號\n網路資訊：http://www.zcegarden.org.tw/\n")
        photo=open('pic/9.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：內雙溪自然公園\n地址：臺北市士林區至善路三段150巷\n網路資訊:http://www.shiaushitou.taipei/ct.asp?xItem=1228368&CtNode=36898&mp=10500C\n")
        update.message.reply_text("想要更多旅遊地點,可以參考此網站：https://www.travel.taipei/zh-tw\n")
        self.go_back(update)

    def on_enter_state41(self, update):
        update.message.reply_text("查詢的結果：\n")
        photo=open('pic/10.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：台北市立動物園\n地址：臺北市文山區新光路二段30號\n網路資訊：http://www.zoo.gov.taipei/\n")
        photo=open('pic/11.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：台北市立天文科學教育館\n地址：臺北市士林區基河路363號\n網路資訊：http://www.tam.gov.taipei/\n")
        photo=open('pic/12.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：國立台灣科學教育館\n地址：臺北市士林區士商路189號\n網路資訊：https://www.ntsec.gov.tw/User/index.aspx\n")
        update.message.reply_text("想要更多旅遊地點,可以參考此網站：https://www.travel.taipei/zh-tw\n")
        self.go_back(update)
##################################################################################################
    def on_enter_state42(self, update):
        update.message.reply_text("查詢的結果：\n")
        photo=open('pic/16.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：林本源園邸\n地址：新北市板橋區西門街9號\n網路資訊：http://www.linfamily.ntpc.gov.tw/\n")
        photo=open('pic/17.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：三峽祖師廟\n地址：新北市三峽區長福街1號\n網路資訊：http://www.longfuyan.org.tw/front/bin/home.phtml\n")
        photo=open('pic/18.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：一滴水紀念館\n地址：新北市淡水區中正路一段6巷30號\n網路資訊：http://www.tamsui.ntpc.gov.tw/content/?parent_id=10247\n")
        update.message.reply_text("想要更多旅遊地點,可以參考此網站：http://emmm.tw/s.php?city=taipei\n")
        self.go_back(update)
    def on_enter_state43(self, update):
        update.message.reply_text("查詢的結果：\n")
        photo=open('pic/19.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：十分瀑布\n地址：新北市平溪區乾坑10號\n網路資訊：http://hantianblog.com/archives/9888\n")
        photo=open('pic/20.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：碧潭\n地址：新北市新店區新店路\n網路資訊：http://wkitty.tw/blog/post/33682715-%E3%80%90%E7%A2%A7%E6%BD%AD%E9%A2%A8%E6%99%AF%E5%8D%80%E4%B8%80%E6%97%A5%E9%81%8A%E3%80%91%E6%83%85%E4%BA%BA%E5%BF%85%E5%8E%BB%EF%BC%8C%E6%84%9B%E7%A5%9E%E9%82%B1%E6%AF%94%E7%89%B9\n")
        photo=open('pic/21.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：挖仔尾自然生態保留區\n地址：新北市八里區\n網路資訊:http://conservation.forest.gov.tw/0000124\n")
        update.message.reply_text("想要更多旅遊地點,可以參考此網站：https://www.google.com.tw/search?sa=N&q=%E6%96%B0%E5%8C%97%E5%B8%82%E6%99%AF%E9%BB%9E&ved=0ahUKEwiE2PD8wZXUAhWCkZQKHRwKBok4FBC7MQgJ&biw=1833&bih=921\n")
        self.go_back(update)

    def on_enter_state44(self, update):
        update.message.reply_text("查詢的結果：\n")
        photo=open('pic/22.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：野柳海洋世界\n地址：新北市萬里區港東路167-3號\n網路資訊：http://www.oceanworld.com.tw/\n")
        photo=open('pic/23.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：滿月圓國家森林遊樂區\n地址：新北市三峽區\n網路資訊：http://recreation.forest.gov.tw/RA/RA_1_1.aspx?RA_ID=0200001\n")
        photo=open('pic/24.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：金山老街\n地址：新北市金山區金包里街\n網路資訊：http://kikinote.net/article/91260.html\n")
        update.message.reply_text("想要更多旅遊地點,可以參考此網站：http://travel.network.com.tw/tourguide/twnmap/newtaipei-city/\n")
        self.go_back(update)
	
####################################################################################################
    def on_enter_state45(self, update):
        update.message.reply_text("查詢的結果：\n")
        photo=open('pic/26.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：陰陽海\n地址：新北市瑞芳區濓新里\n網路資訊：http://guide.easytravel.com.tw/scenic/2518\n")
        photo=open('pic/27.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：外木山濱海風景區\n地址：基隆市中山區協和街\n網路資訊：http://www.northguan-nsa.gov.tw/user/Article.aspx?Lang=1&SNo=04005326\n")
        photo=open('pic/28.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：望幽谷\n地址：基隆市中正區八斗子\n網路資訊：http://okgo.tw/butyview.html?id=451\n")
        update.message.reply_text("想要更多旅遊地點,可以參考此網站：https://www.tripadvisor.com.tw/Attractions-g317130-Activities-Keelung.html\n")
        self.go_back(update)

####################################################################################################
    def on_enter_state46(self, update):
        update.message.reply_text("查詢的結果：\n")
        photo=open('pic/29.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：大溪老街-普濟堂\n地址：桃園縣普濟路124號\n網路資訊：http://puji.tw/\n")
        update.message.reply_text("想要更多旅遊地點,可以參考此網址：https://www.tripadvisor.com.tw/Attractions-g297912-Activities-Taoyuan.html\n")
        self.go_back(update)
    def on_enter_state47(self, update):
        update.message.reply_text("查詢的結果：\n")
        photo=open('pic/30.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：石門水庫風景區\n地址：桃園市龍潭區佳安里佳安路2號\n網路資訊：http://okgo.tw/butyview.html?id=162\n")
        update.message.reply_text("想要更多旅遊地點,可以參考此網站：https://www.tripadvisor.com.tw/Attractions-g297912-Activities-Taoyuan.html\n")
        self.go_back(update)

    def on_enter_state48(self, update):
        update.message.reply_text("查詢的結果：\n")
        photo=open('pic/31.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：小人國主題樂園\n地址：桃園縣龍潭鄉高原村橫岡下60-2號\n網路資訊：http://www.woc.com.tw/\n")
        update.message.reply_text("想要更多旅遊地點,可以參考此網站：https://www.tripadvisor.com.tw/Attractions-g297912-Activities-Taoyuan.html\n")
        self.go_back(update)

####################################################################################################
    def on_enter_state49(self, update):
        update.message.reply_text("查詢的結果：\n")
        photo=open('pic/32.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：大霸尖山\n地址：新竹縣\n網路資訊：http://tw.hiking.biji.co/index.php?q=news&act=info&id=7650\n")
        update.message.reply_text("想要更多旅遊地點,可以參考此網站：http://travel.network.com.tw/main/travel/hsinchucounty/\n")
        self.go_back(update)
    def on_enter_state50(self, update):
        update.message.reply_text("查詢的結果：\n")
        photo=open('pic/33.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：北埔慈天宮\n地址：新竹縣北埔鄉北埔街1號\n網路資訊：http://www.hchcc.gov.tw/ch/06culture/cul_02_main.asp?bull_id=1054\n")
        update.message.reply_text("想要更多旅遊地點,可以參考此網站：http://travel.network.com.tw/main/travel/hsinchucounty/\n")
        self.go_back(update)

    def on_enter_state51(self, update):
        update.message.reply_text("查詢的結果：\n")
        photo=open('pic/34.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：六福村主題遊樂園\n地址：新竹縣關西鎮仁安里拱子溝60號\n網路資訊：http://www1.leofoo.com.tw/village/\n")
        update.message.reply_text("想要更多旅遊地點,可以參考此網站：http://travel.network.com.tw/main/travel/hsinchucounty/\n")
        self.go_back(update)

####################################################################################################
    def on_enter_state52(self, update):
        update.message.reply_text("查詢的結果：\n")
        photo=open('pic/35.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：新竹都城隍廟\n地址：新竹市北區中山路75號\n網路資訊：http://www.weiling.org.tw/\n")
        update.message.reply_text("想要更多旅遊地點,可以參考此網站：http://travel.network.com.tw/tourguide/twnmap/hsinchucity/\n")
        self.go_back(update)
    def on_enter_state53(self, update):
        update.message.reply_text("查詢的結果：\n")
        photo=open('pic/36.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：十八尖山\n地址：新竹市東區\n網路資訊：http://bob20842.pixnet.net/blog/post/387357718-%E6%96%B0%E7%AB%B9%E6%97%85%E9%81%8A%E6%99%AF%E9%BB%9E-%E7%B6%A0%E6%98%A0%E7%9B%8E%E7%84%B6%E7%9A%84%E5%8D%81%E5%85%AB%E5%B0%96%E5%B1%B1%E6%AD%A5%E9%81%93%28%E6%95%A3%E6%AD%A5\n")
        update.message.reply_text("想要更多旅遊地點,可以參考此網站：http://travel.network.com.tw/tourguide/twnmap/hsinchucity/\n")
        self.go_back(update)

    def on_enter_state54(self, update):
        update.message.reply_text("查詢的結果：\n")
        photo=open('pic/37.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：新竹市立動物園\n地址：新竹市東區博愛街111號\n網路資訊：http://zoo.e-tobe.com/\n")
        update.message.reply_text("想要更多旅遊地點,可以參考此網站：http://travel.network.com.tw/tourguide/twnmap/hsinchucity/\n")
        self.go_back(update)

####################################################################################################
    def on_enter_state55(self, update):
        update.message.reply_text("查詢的結果：\n")
        photo=open('pic/38.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：國立傳統藝術中心\n地址：宜蘭縣五結鄉五濱路二段201號\n網路資訊：http://www.ncfta.gov.tw/\n")
        update.message.reply_text("想要更多旅遊地點,可以參考此網站：https://asiayo.com/event/yilan_twfit.html?utm_source=google_adwords&utm_campaign=47165959852&utm_medium=cpc&utm_term=%E5%AE%9C%E8%98%AD%E6%99%AF%E9%BB%9E&gclid=CjwKEAjwja_JBRD8idHpxaz0t3wSJAB4rXW5VHyYcGCEGcOMsm8S_reaKRp5dh9VCxvsxgRFNRak4hoCX5fw_wcB\n")
        self.go_back(update)
    def on_enter_state56(self, update):
        update.message.reply_text("查詢的結果：\n")
        photo=open('pic/39.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：龜山島\n地址：宜蘭縣外海\n網路資訊：https://www.ez666.com/hwachyi/content/mountain1.php\n")
        update.message.reply_text("想要更多旅遊地點,可以參考此網站：https://asiayo.com/event/yilan_twfit.html?utm_source=google_adwords&utm_campaign=47165959852&utm_medium=cpc&utm_term=%E5%AE%9C%E8%98%AD%E6%99%AF%E9%BB%9E&gclid=CjwKEAjwja_JBRD8idHpxaz0t3wSJAB4rXW5VHyYcGCEGcOMsm8S_reaKRp5dh9VCxvsxgRFNRak4hoCX5fw_wcB\n")
        self.go_back(update)

    def on_enter_state57(self, update):
        update.message.reply_text("查詢的結果：\n")
        photo=open('pic/40.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：幾米公園\n地址：宜蘭縣宜蘭市宜興路一段240號\n網路資訊：http://aerrr1.pixnet.net/blog/post/31465159-%E3%80%90%E5%AE%9C%E8%98%AD%E3%80%91%E5%B9%BE%E7%B1%B3%E5%BB%A3%E5%A0%B4-%28%E5%B9%BE%E7%B1%B3%E4%B8%BB%E9%A1%8C%E5%85%AC%E5%9C%92%29%E3%80%82%E6%8B%8D%E7%85%A7%E5%A5%BD%E6%99%AF\n")
        update.message.reply_text("想要更多旅遊地點,可以參考此網站：https://asiayo.com/event/yilan_twfit.html?utm_source=google_adwords&utm_campaign=47165959852&utm_medium=cpc&utm_term=%E5%AE%9C%E8%98%AD%E6%99%AF%E9%BB%9E&gclid=CjwKEAjwja_JBRD8idHpxaz0t3wSJAB4rXW5VHyYcGCEGcOMsm8S_reaKRp5dh9VCxvsxgRFNRak4hoCX5fw_wcB\n")
        self.go_back(update)

####################################################################################################
    def on_enter_state58(self, update):
       	update.message.reply_text("我推薦這些網址,看看吧：\nhttp://rainbow7601.pixnet.net/blog/post/62580410-%5B%E8%8B%97%E6%A0%97%E6%99%AF%E9%BB%9E%E6%8E%A8%E8%96%A6%5D-15%E5%80%8B%E7%B2%BE%E8%8F%AF%E6%99%AF%E9%BB%9E~%E4%B8%89%E5%A4%A7%E4%B8%BB%E9%A1%8C%E4%B9%8B%E6%97%85%E8%A6%8F")
       	update.message.reply_text("http://okgo.tw/buty/miaoli.html")
        self.go_back(update)
    def on_enter_state59(self, update):
        update.message.reply_text("想要哪種種類呢？")
        update.message.reply_text("1.人文\n")
        photo=open('pic/41.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("2.自然\n")
        photo=open('pic/42.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("3.親子共遊\n")
        photo=open('pic/43.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
####################################################################################################
    def on_enter_state60(self, update):
        update.message.reply_text("我推薦這個網址看看吧\nhttp://rainbow7601.pixnet.net/blog/post/46662128-%5B%E5%8F%B0%E4%B8%AD%E6%99%AF%E9%BB%9E%E6%8E%A8%E8%96%A6%5D8%E5%80%8B%E6%B5%B7%E7%B7%9A%E6%99%AF%E9%BB%9E%E3%80%8121%E5%80%8B%E5%B8%82%E5%8D%80%E6%99%AF%E9%BB%9E%2A%E8%B6%85\n")
        update.message.reply_text("http://nanacobaby.pixnet.net/blog/post/49951710-%E5%8F%B0%E4%B8%AD%E6%97%85%E9%81%8A%E6%99%AF%E9%BB%9E%E6%87%B6%E4%BA%BA%E5%8C%85~%E4%B8%80%E6%97%A5%E9%81%8A%E3%80%81%E4%BA%8C%E6%97%A5%E9%81%8A%E8%A1%8C%E7%A8%8B%E6%8E%A8")
        self.go_back(update)
    def on_enter_state61(self, update):
        update.message.reply_text("想要哪種種類呢？")
        update.message.reply_text("1.人文\n")
        photo=open('pic/44.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("2.自然\n")
        photo=open('pic/45.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("3.親子共遊\n")
        photo=open('pic/46.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
###################################################################################################
    def on_enter_state62(self, update):
        update.message.reply_text("我推薦這個網址看看吧\nhttp://kiwi77720.pixnet.net/blog/post/63312994-%E3%80%90%E5%BD%B0%E5%8C%96%E7%B8%A3%E5%B8%82%E6%97%85%E9%81%8A%E6%99%AF%E9%BB%9E%E3%80%91%E9%83%A8%E8%90%BD%E5%AE%A2%E6%97%85%E9%81%8A%E9%81%94%E4%BA%BA%E7%A7%81%E6%88%BF%E7%A7%98\n")
        update.message.reply_text("http://nana0032458.pixnet.net/blog/post/58263406-%E3%80%90%E5%BD%B0%E5%8C%96%E6%99%AF%E9%BB%9E%E3%80%91%E7%B2%BE%E9%81%B8100%E5%80%8B%E5%BD%B0%E5%8C%96%E6%99%AF%E9%BB%9E%E6%94%BB%E7%95%A5%E2%94%82%E5%BD%B0%E5%8C%96%E4%B8%80")
        self.go_back(update)
    def on_enter_state63(self, update):
        update.message.reply_text("想要哪種種類呢？")
        update.message.reply_text("1.人文\n")
        photo=open('pic/47.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("2.自然\n")
        photo=open('pic/48.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("3.親子共遊\n")
        photo=open('pic/49.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
##################################################################################################
    def on_enter_state64(self, update):
        update.message.reply_text("我推薦這個網址看看吧\nhttp://yoke918.com/?tag=%E9%9B%B2%E6%9E%97%E6%97%85%E9%81%8A%E6%99%AF%E9%BB%9E\n")
        update.message.reply_text("http://anquine7.pixnet.net/blog/post/389051705-%5B%E9%9B%B2%E6%9E%97%E3%80%82%E6%87%B6%E4%BA%BA%E5%8C%85%5D-%E9%9B%B2%E6%9E%97%E7%99%BE%E5%A4%A7%E4%BA%AE%E9%BB%9E%E8%BF%BD%E8%BF%BD%E8%BF%BD%EF%BC%81%E5%9C%A8%E5%9C%B0%E7%8B%BC")
        self.go_back(update)
    def on_enter_state65(self, update):
        update.message.reply_text("想要哪種種類呢？")
        update.message.reply_text("1.人文\n")
        photo=open('pic/50.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("2.自然\n")
        photo=open('pic/51.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("3.親子共遊\n")
        photo=open('pic/52.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
################################################################################################
    def on_enter_state66(self, update):
        update.message.reply_text("我推薦這個網址看看吧\nhttp://traveler135.pixnet.net/blog/post/208265182-%E5%8D%97%E6%8A%95%E6%99%AF%E9%BB%9E%E4%B8%80%E6%97%A5%E9%81%8A%2C%E5%8D%97%E6%8A%95%E4%B8%80%E6%97%A5%E9%81%8A%2C%E5%9F%94%E9%87%8C%E4%B8%80%E6%97%A5%E9%81%8A%E6%8E%A8%E8%96%A6\n")
        update.message.reply_text("http://rainbow7601.pixnet.net/blog/post/53436322-%5B%E5%8D%97%E6%8A%95%E6%99%AF%E9%BB%9E%E6%8E%A8%E8%96%A6%5D-23%E5%80%8B%E7%B2%BE%E8%8F%AF%E6%99%AF%E9%BB%9E~%E4%BA%94%E5%A4%A7%E4%B8%BB%E9%A1%8C%E4%B9%8B%E6%97%85%E8%A6%8F")
        self.go_back(update)
    def on_enter_state67(self, update):
        update.message.reply_text("想要哪種種類呢？")
        update.message.reply_text("1.人文\n")
        photo=open('pic/53.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("2.自然\n")
        photo=open('pic/54.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("3.親子共遊\n")
        photo=open('pic/55.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
###################################################################################################
    def on_enter_state68(self, update):
        update.message.reply_text("查詢的結果：\n")
        photo=open('pic/41.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：雲洞宮\n地址：頭屋鄉鳴鳳村三湖6鄰120號\n網路資訊：http://www.miaoli.gov.tw/touwu_travel/gmap/index-1.php?m2=10&id=17\n")
        update.message.reply_text("想要更多旅遊地點,可以參考此網站：http://okgo.tw/buty/miaoli.html\n")
        self.go_back(update)
    def on_enter_state69(self, update):
        update.message.reply_text("查詢的結果：\n")
        photo=open('pic/42.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：向天湖\n地址：南庄鄉東河村\n網路資訊：http://viablog.okmall.tw/blogview.php?blogid=1559\n")
        update.message.reply_text("想要更多旅遊地點,可以參考此網站：http://okgo.tw/buty/miaoli.html\n")
        self.go_back(update)

    def on_enter_state70(self, update):
        update.message.reply_text("查詢的結果：\n")
        photo=open('pic/43.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：飛牛牧場\n地址：通霄鎮南和里166號\n網路資訊：http://www.flyingcow.com.tw/\n")
        update.message.reply_text("想要更多旅遊地點,可以參考此網站：http://okgo.tw/buty/miaoli.html\n")
        self.go_back(update)

####################################################################################################
    def on_enter_state71(self, update):
        update.message.reply_text("查詢的結果：\n")
        photo=open('pic/44.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：路思義教堂\n地址：台中市西屯區台灣大道四段1727號\n網路資訊：http://okgo.tw/butyview.html?id=2056\n")
        update.message.reply_text("想要更多旅遊地點,可以參考此網站：http://anny3805201314.pixnet.net/blog/post/219387993-%E5%8F%B0%E4%B8%AD%E5%A5%BD%E5%A5%BD%E7%8E%A9~%E5%A4%A7%E5%8F%B0%E4%B8%AD%E6%99%AF%E9%BB%9E%E4%B8%80%E8%A6%BD%E8%A1%A8(106-05-02%E6%9B%B4%E6%96%B0)\n")
        self.go_back(update)
    def on_enter_state72(self, update):
        update.message.reply_text("查詢的結果：\n")
        photo=open('pic/45.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：雪山\n地址：山區\n網路資訊：http://www.spnp.gov.tw/Article.aspx?a=i%2ByYs%2FIf4hs%3D\n")
        update.message.reply_text("想要更多旅遊地點,可以參考此網站：http://anny3805201314.pixnet.net/blog/post/219387993-%E5%8F%B0%E4%B8%AD%E5%A5%BD%E5%A5%BD%E7%8E%A9~%E5%A4%A7%E5%8F%B0%E4%B8%AD%E6%99%AF%E9%BB%9E%E4%B8%80%E8%A6%BD%E8%A1%A8(106-05-02%E6%9B%B4%E6%96%B0)\n")
        self.go_back(update)

    def on_enter_state73(self, update):
        update.message.reply_text("查詢的結果：\n")
        photo=open('pic/46.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：國立自然科學博物館\n地址：台中市北區館前路1號\n網路資訊：http://www.nmns.edu.tw/\n")
        update.message.reply_text("想要更多旅遊地點,可以參考此網站：http://anny3805201314.pixnet.net/blog/post/219387993-%E5%8F%B0%E4%B8%AD%E5%A5%BD%E5%A5%BD%E7%8E%A9~%E5%A4%A7%E5%8F%B0%E4%B8%AD%E6%99%AF%E9%BB%9E%E4%B8%80%E8%A6%BD%E8%A1%A8(106-05-02%E6%9B%B4%E6%96%B0)\n")
        self.go_back(update)

####################################################################################################
    def on_enter_state74(self, update):
        update.message.reply_text("查詢的結果：\n")
        photo=open('pic/47.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：鹿港天后宮\n地址：彰化縣鹿港鎮中山路430號\n網路資訊：http://www.lugangmazu.org/\n")
        update.message.reply_text("想要更多旅遊地點,可以參考此網站：http://blog.cutebox.org/%E5%BD%B0%E5%8C%96%E4%B8%80%E6%97%A5%E9%81%8A\n")
        self.go_back(update)
    def on_enter_state75(self, update):
        update.message.reply_text("查詢的結果：\n")
        photo=open('pic/48.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：八卦山\n地址：彰化山區\n網路資訊：http://travel.network.com.tw/tourguide/point/showpage/1.html\n")
        update.message.reply_text("想要更多旅遊地點,可以參考此網站：http://blog.cutebox.org/%E5%BD%B0%E5%8C%96%E4%B8%80%E6%97%A5%E9%81%8A\n")
        self.go_back(update)

    def on_enter_state76(self, update):
        update.message.reply_text("查詢的結果：\n")
        photo=open('pic/49.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：百果山 溜滑梯\n地址：彰化縣員林市出水巷\n網路資訊：http://blog.xuite.net/bobowin/me/249560234-%E3%80%8A+%E5%BD%B0%E5%8C%96%E8%A6%AA%E5%AD%90%E6%99%AF%E9%BB%9E+%E3%80%8B%E5%BD%B0%E5%8C%96%E7%99%BE%E6%9E%9C%E5%B1%B1%E5%85%A8%E5%8F%B0%E6%9C%80%E9%95%B7%E6%BA%9C%E6%BB%91%E6%A2%AF~+45%E5%BA%A6%E6%96%9C%E5%BA%A6%E8%AE%93%E4%BD%A0%E6%AD%A2%E4%B8%8D%E4%BD%8F%E5%B0%96%E5%8F%AB\n")
        update.message.reply_text("想要更多旅遊地點,可以參考此網站：http://blog.cutebox.org/%E5%BD%B0%E5%8C%96%E4%B8%80%E6%97%A5%E9%81%8A\n")
        self.go_back(update)

####################################################################################################
    def on_enter_state77(self, update):
        update.message.reply_text("查詢的結果：\n")
        photo=open('pic/50.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：北港朝天宮\n地址：雲林縣北港鎮中山路178號\n網路資訊：http://www.matsu.org.tw/\n")
        update.message.reply_text("想要更多旅遊地點,可以參考此網站：http://greenmarch0315.pixnet.net/blog/post/192108243-%E2%97%86%E3%80%90%E9%9B%B2%E6%9E%97%E6%97%85%E9%81%8A%E6%99%AF%E9%BB%9E%E6%87%B6%E4%BA%BA%E5%8C%85%E3%80%91%E5%81%87%E6%9C%9F%E4%BD%95%E8%99%95%E5%8E%BB%EF%BC%9F%E4%BE%86%E9%9B%B2\n")
        self.go_back(update)
    def on_enter_state78(self, update):
        update.message.reply_text("查詢的結果：\n")
        photo=open('pic/51.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：古坑綠色隧道\n地址：雲林縣古坑鄉湳仔村湳仔路\n網路資訊：http://s045488.pixnet.net/blog/post/73559716-%5B%E9%9B%B2%E6%9E%97%E6%99%AF%E9%BB%9E%5D%E5%8F%A4%E5%9D%91%E7%B6%A0%E8%89%B2%E9%9A%A7%E9%81%93%E2%99%A5%E6%88%91%E5%AE%9B%E5%A6%82%E6%BC%AB%E6%AD%A5%E5%9C%A8%E6%B3%95%E5%9C%8B\n")
        update.message.reply_text("想要更多旅遊地點,可以參考此網站：http://greenmarch0315.pixnet.net/blog/post/192108243-%E2%97%86%E3%80%90%E9%9B%B2%E6%9E%97%E6%97%85%E9%81%8A%E6%99%AF%E9%BB%9E%E6%87%B6%E4%BA%BA%E5%8C%85%E3%80%91%E5%81%87%E6%9C%9F%E4%BD%95%E8%99%95%E5%8E%BB%EF%BC%9F%E4%BE%86%E9%9B%B2\n")
        self.go_back(update)

    def on_enter_state79(self, update):
        update.message.reply_text("查詢的結果：\n")
        photo=open('pic/52.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：劍湖山世界\n地址：雲林縣古坑鄉永光村大湖口67號\n網路資訊：http://www.janfusun.com.tw/\n")
        update.message.reply_text("想要更多旅遊地點,可以參考此網站：http://greenmarch0315.pixnet.net/blog/post/192108243-%E2%97%86%E3%80%90%E9%9B%B2%E6%9E%97%E6%97%85%E9%81%8A%E6%99%AF%E9%BB%9E%E6%87%B6%E4%BA%BA%E5%8C%85%E3%80%91%E5%81%87%E6%9C%9F%E4%BD%95%E8%99%95%E5%8E%BB%EF%BC%9F%E4%BE%86%E9%9B%B2\n")
        self.go_back(update)

####################################################################################################
    def on_enter_state80(self, update):
        update.message.reply_text("查詢的結果：\n")
        photo=open('pic/53.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：台灣影城之桃太郎村\n地址：南投縣竹山鎮保甲路186號\n網路資訊：http://fbuon2881.pixnet.net/blog/post/207830272-%E3%80%90%E5%8D%97%E6%8A%95%E7%AB%B9%E5%B1%B1%E3%80%91%E7%AB%B9%E5%B1%B1%E6%A1%83%E5%A4%AA%E9%83%8E%E6%9D%91%E5%8F%B0%E7%81%A3%E5%BD%B1%E5%9F%8E%E5%89%8D%E9%80%B2%E6%97%A5%E6%9C%AC\n")
        update.message.reply_text("想要更多旅遊地點,可以參考此網站：http://bulanini.pixnet.net/blog/post/171087768-%E5%8D%97%E6%8A%95%E6%99%AF%E9%BB%9E%E6%8E%A8%E8%96%A6-%E5%8D%97%E6%8A%95%E6%97%85%E9%81%8A%E6%99%AF%E9%BB%9E-%E5%8D%97%E6%8A%95%E7%86%B1%E9%96%80%E6%99%AF%E9%BB%9E\n")
        self.go_back(update)
    def on_enter_state81(self, update):
        update.message.reply_text("查詢的結果：\n")
        photo=open('pic/54.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：武嶺\n地址：南投縣仁愛鄉\n網路資訊：http://travel.network.com.tw/tourguide/point/showpage/102399.html\n")
        update.message.reply_text("想要更多旅遊地點,可以參考此網站：http://bulanini.pixnet.net/blog/post/171087768-%E5%8D%97%E6%8A%95%E6%99%AF%E9%BB%9E%E6%8E%A8%E8%96%A6-%E5%8D%97%E6%8A%95%E6%97%85%E9%81%8A%E6%99%AF%E9%BB%9E-%E5%8D%97%E6%8A%95%E7%86%B1%E9%96%80%E6%99%AF%E9%BB%9E\n")
        self.go_back(update)

    def on_enter_state82(self, update):
        update.message.reply_text("查詢的結果：\n")
        photo=open('pic/55.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：九族文化村\n地址：南投縣魚池鄉金天巷45號\n網路資訊：http://www.nine.com.tw/\n")
        update.message.reply_text("想要更多旅遊地點,可以參考此網站：http://bulanini.pixnet.net/blog/post/171087768-%E5%8D%97%E6%8A%95%E6%99%AF%E9%BB%9E%E6%8E%A8%E8%96%A6-%E5%8D%97%E6%8A%95%E6%97%85%E9%81%8A%E6%99%AF%E9%BB%9E-%E5%8D%97%E6%8A%95%E7%86%B1%E9%96%80%E6%99%AF%E9%BB%9E\n")
        self.go_back(update)

####################################################################################################
    def on_enter_state83(self, update):
        update.message.reply_text("我推薦這個網址看看吧\nhttp://tinachiang0824.pixnet.net/blog/post/426844655-%E5%98%89%E7%BE%A9%E4%B8%80%E6%97%A5%E6%97%85%E9%81%8A%E6%99%AF%E9%BB%9E%E6%8E%A8%E8%96%A6-%E6%88%91%E5%98%89%E5%A5%BD%E5%A5%BD%E7%8E%A9%282017.03.26%E6%96%B0\n")
        update.message.reply_text("http://jasmine0425.pixnet.net/blog/post/330499952-%E2%96%8C%E9%81%8A%E8%A8%98-%E2%96%8C%E5%98%89%E7%BE%A9%E7%B8%A3%E5%B8%82%E5%A5%BD%E5%A5%BD%E7%8E%A9-%E6%97%85%E9%81%8A%E6%99%AF%E9%BB%9E%E5%A4%A7%E7%B8%BD%E6%94%AC%28%E5%B8%82")
        self.go_back(update)
    def on_enter_state84(self, update):
        update.message.reply_text("想要哪種種類呢？")
        update.message.reply_text("1.人文\n")
        photo=open('pic/56.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("2.自然\n")
        photo=open('pic/57.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("3.親子共遊\n")
        photo=open('pic/58.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()

###################################################################################################
    def on_enter_state85(self, update):
        update.message.reply_text("我推薦這個網址看看吧\nhttps://www.tripadvisor.com.tw/Attractions-g297904-Activities-Chiayi.html\n")
        update.message.reply_text("http://travel.chiayi.gov.tw/TC/spotsList.aspx")
        self.go_back(update)
    def on_enter_state86(self, update):
        update.message.reply_text("想要哪種種類呢？")
        update.message.reply_text("1.人文\n")
        photo=open('pic/59.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("2.自然\n")
        photo=open('pic/60.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("3.親子共遊\n")
        photo=open('pic/61.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()

###################################################################################################
    def on_enter_state87(self, update):
        update.message.reply_text("我推薦這個網址看看吧\nhttp://blog.xuite.net/shoran63/blog/309702150-%E3%80%90%E6%87%B6%E4%BA%BA%E5%B0%88%E7%94%A8%E3%80%91%E5%8F%B0%E5%8D%97%E5%BF%85%E9%81%8A%E5%8D%81%E5%A4%A7%E7%89%B9%E8%89%B2%E6%99%AF%E9%BB%9E\n")
        update.message.reply_text("https://tw.bring-you.info/tainan-travel-tips")
       	f=open('video/1.mp4','rb+')
       	update.message.reply_video(f)
        f.close()	        
       	self.go_back(update)

    def on_enter_state88(self, update):
        update.message.reply_text("想要哪種種類呢？")
        update.message.reply_text("1.人文\n")
        photo=open('pic/62.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("2.自然\n")
        photo=open('pic/63.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("3.親子共遊\n")
        photo=open('pic/64.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()

###################################################################################################
    def on_enter_state89(self, update):
        update.message.reply_text("我推薦這個網址看看吧\nhttp://rainbow7601.pixnet.net/blog/post/62615732-%5B%E9%AB%98%E9%9B%84%E6%99%AF%E9%BB%9E%E6%8E%A8%E8%96%A6%5D-23%E5%80%8B%E7%B2%BE%E8%8F%AF%E6%99%AF%E9%BB%9E~%E4%BA%94%E5%A4%A7%E4%B8%BB%E9%A1%8C%E4%B9%8B%E6%97%85%E8%A6%8F\n")
        update.message.reply_text("http://nellydyu.tw/blog/post/37301069-%E3%80%8E%E6%97%85%E9%81%8A%E3%80%8F%E2%98%BC%E6%94%BE%E5%81%87%E5%9B%89%EF%BC%81%E9%AB%98%E9%9B%84%E5%8F%AF%E4%BB%A5%E5%8E%BB%E5%93%AA%E8%A3%A1%E9%81%8A%E4%BE%86%E9%81%8A%E5%8E%BB")
        self.go_back(update)
    def on_enter_state90(self, update):
        update.message.reply_text("想要哪種種類呢？")
        update.message.reply_text("1.人文\n")
        photo=open('pic/65.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("2.自然\n")
        photo=open('pic/66.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("3.親子共遊\n")
        photo=open('pic/67.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()

###################################################################################################
    def on_enter_state91(self, update):
        update.message.reply_text("我推薦這個網址看看吧\nhttps://taiwantour.info/%E5%B1%8F%E6%9D%B1%E5%90%83%E5%96%9D%E7%8E%A9%E6%A8%82%EF%BC%8E%E6%99%AF%E9%BB%9E%EF%BC%8E%E7%BE%8E%E9%A3%9F%EF%BC%8E%E6%B0%91%E5%AE%BF%E6%8E%A8%E8%96%A6%E6%87%B6%E4%BA%BA%E5%8C%85/\n")
        update.message.reply_text("http://yoke918.com/?cat=59")
        self.go_back(update)
    def on_enter_state92(self, update):
        update.message.reply_text("想要哪種種類呢？")
        update.message.reply_text("1.人文\n")
        photo=open('pic/68.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("2.自然\n")
        photo=open('pic/69.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("3.親子共遊\n")
        photo=open('pic/70.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()

###################################################################################################
    def on_enter_state93(self, update):
        update.message.reply_text("查詢的結果：\n")
        photo=open('pic/56.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：新港奉天宮\n地址：嘉義縣新港鄉新民路53號\n網路資訊：http://www.hsinkangmazu.org.tw/news.asp\n")
        update.message.reply_text("想要更多旅遊地點,可以參考此網站：http://emmm.tw/s.php?city=chiayi\n")
        self.go_back(update)
    def on_enter_state94(self, update):
        update.message.reply_text("查詢的結果：\n")
        photo=open('pic/57.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：阿里山\n地址：嘉義縣阿里山鄉中正村59號\n網路資訊：http://www.ali-nsa.net/user/Main.aspx?Lang=1\n")
        update.message.reply_text("想要更多旅遊地點,可以參考此網站：http://emmm.tw/s.php?city=chiayi\n")
        self.go_back(update)

    def on_enter_state95(self, update):
        update.message.reply_text("查詢的結果：\n")
        photo=open('pic/58.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：竹崎親水公園\n地址：嘉義縣竹崎鄉中正路96號\n網路資訊：http://okgo.tw/butyview.html?id=01092\n")
        update.message.reply_text("想要更多旅遊地點,可以參考此網站：http://emmm.tw/s.php?city=chiayi\n")
        self.go_back(update)

####################################################################################################
    def on_enter_state96(self, update):
        update.message.reply_text("查詢的結果：\n")
        photo=open('pic/59.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：嘉義舊監獄\n地址：嘉義市東區維新路140號\n網路資訊：http://mimg47.pixnet.net/blog/post/5521277-%E3%80%90%E5%98%89%E7%BE%A9%E6%99%AF%E9%BB%9E%E3%80%91%E5%98%89%E7%BE%A9%E8%88%8A%E7%9B%A3%E7%8D%84%EF%BC%8E%E7%8D%84%E6%94%BF%E5%8D%9A%E7%89%A9%E9%A4%A8%EF%BC%9A%E5%85%A8%E5%8F%B0\n")
        update.message.reply_text("想要更多旅遊地點,可以參考此網站：http://yoke918.com/?p=2784\n")
        self.go_back(update)
    def on_enter_state97(self, update):
        update.message.reply_text("查詢的結果：\n")
        photo=open('pic/60.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：蘭潭風景區\n地址：嘉義市東區小雅路\n網路資訊：http://travel.network.com.tw/tourguide/point/showpage/1057.html\n")
        update.message.reply_text("想要更多旅遊地點,可以參考此網站：http://yoke918.com/?p=2784\n")
        self.go_back(update)

    def on_enter_state98(self, update):
        update.message.reply_text("查詢的結果：\n")
        photo=open('pic/61.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：嘉義鐵道藝術村\n地址：嘉義市西區北興街37之10號開放\n網路資訊：http://www.cabcy.gov.tw/railway/\n")
        update.message.reply_text("想要更多旅遊地點,可以參考此網站：http://yoke918.com/?p=2784\n")
        self.go_back(update)

####################################################################################################
    def on_enter_state99(self, update):
        update.message.reply_text("查詢的結果：\n")
        photo=open('pic/62.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：赤崁樓\n地址：台南市中西區民族路二段212號\n網路資訊：http://www.premier.com.tw/Touring/chikanlou.htm\n")
        update.message.reply_text("想要更多旅遊地點,可以參考此網站：https://kgs710522.blogspot.com/2014/12/blog-post.html\n")
        self.go_back(update)
    def on_enter_state100(self, update):
        update.message.reply_text("查詢的結果：\n")
        photo=open('pic/63.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：關子嶺溫泉\n地址：台南市白河區\n網路資訊：http://guanzi.emmm.tw/\n")
        update.message.reply_text("想要更多旅遊地點,可以參考此網站：https://kgs710522.blogspot.com/2014/12/blog-post.html\n")
        self.go_back(update)

    def on_enter_state101(self, update):
        update.message.reply_text("查詢的結果：\n")
        photo=open('pic/64.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：台江國家公園\n地址：台南市安南區四草大道\n網路資訊：http://www.tjnp.gov.tw/index.aspx\n")
        update.message.reply_text("想要更多旅遊地點,可以參考此網站：https://kgs710522.blogspot.com/2014/12/blog-post.html\n")
        self.go_back(update)

####################################################################################################
    def on_enter_state102(self, update):
        update.message.reply_text("查詢的結果：\n")
        photo=open('pic/65.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：佛陀紀念館\n地址：高雄市大樹區統嶺里統嶺路1號\n網路資訊：http://www.fgsbmc.org.tw/index.aspx\n")
        update.message.reply_text("想要更多旅遊地點,可以參考此網站：http://ksdelicacy.pixnet.net/blog/post/59598319-%E9%AB%98%E9%9B%84%E6%97%85%E9%81%8A%E7%B2%BE%E9%81%B8%EF%BC%81%E4%B8%80%E5%B9%B4%E5%9B%9B%E5%AD%A3%E7%8E%A9%E4%B8%8D%E5%81%9C%282017-03-05%29---%E9%AB%98\n")
        self.go_back(update)
    def on_enter_state103(self, update):
        update.message.reply_text("查詢的結果：\n")
        photo=open('pic/66.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：田寮月世界\n地址：高雄市山區\n網路資訊：http://becky-photo.com/kaohsiung0225/\n")
        update.message.reply_text("想要更多旅遊地點,可以參考此網站：http://ksdelicacy.pixnet.net/blog/post/59598319-%E9%AB%98%E9%9B%84%E6%97%85%E9%81%8A%E7%B2%BE%E9%81%B8%EF%BC%81%E4%B8%80%E5%B9%B4%E5%9B%9B%E5%AD%A3%E7%8E%A9%E4%B8%8D%E5%81%9C%282017-03-05%29---%E9%AB%98\n")
        self.go_back(update)

    def on_enter_state104(self, update):
        update.message.reply_text("查詢的結果：\n")
        photo=open('pic/67.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：美濃民俗村\n地址：高雄市美濃區中山路二段421巷80號\n網路資訊：http://www.meinung-folk-village.com.tw/\n")
        update.message.reply_text("想要更多旅遊地點,可以參考此網站：http://ksdelicacy.pixnet.net/blog/post/59598319-%E9%AB%98%E9%9B%84%E6%97%85%E9%81%8A%E7%B2%BE%E9%81%B8%EF%BC%81%E4%B8%80%E5%B9%B4%E5%9B%9B%E5%AD%A3%E7%8E%A9%E4%B8%8D%E5%81%9C%282017-03-05%29---%E9%AB%98\n")
        self.go_back(update)

####################################################################################################
    def on_enter_state105(self, update):
        update.message.reply_text("查詢的結果：\n")
        photo=open('pic/68.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：台灣原住民族文化園區\n地址：屏東縣瑪家鄉北葉村風景104號\n網路資訊：http://www.tacp.gov.tw/home01.aspx?ID=1\n")
        update.message.reply_text("想要更多旅遊地點,可以參考此網站：https://www.walkerland.com.tw/subject/view/101353\n")
        self.go_back(update)
    def on_enter_state106(self, update):
        update.message.reply_text("查詢的結果：\n")
        photo=open('pic/69.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：船帆石\n地址：屏東縣恆春鎮\n網路資訊：http://www.ktnp.gov.tw/News_Content2.aspx?n=85E1E406503C665B&sms=C88B5251F308CE96&s=AF9EF3A8785FF5A8\n")
        update.message.reply_text("想要更多旅遊地點,可以參考此網站：https://www.walkerland.com.tw/subject/view/101353\n")
        self.go_back(update)

    def on_enter_state107(self, update):
        update.message.reply_text("查詢的結果：\n")
        photo=open('pic/70.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：國立海洋生物博物館\n地址：屏東縣車城鄉後灣路2號\n網路資訊：http://www.nmmba.gov.tw/\n")
        update.message.reply_text("想要更多旅遊地點,可以參考此網站：https://www.walkerland.com.tw/subject/view/101353\n")
        self.go_back(update)

####################################################################################################
    def on_enter_state108(self, update):
        update.message.reply_text("我推薦這個網址看看吧\nhttp://naughtyangel.pixnet.net/blog/post/43251856-%E8%8A%B1%E8%93%AE%E5%BF%85%E5%90%83%E3%80%81%E5%BF%85%E7%8E%A9%E3%80%81%E5%BF%85%E4%BD%8F%E5%8E%BB%E8%99%95%EF%BC%8C88%E8%99%95%E4%B8%8D%E8%97%8F%E7%A7%81%E5%A4%A7%E5%85%AC\n")
        update.message.reply_text("https://www.tripadvisor.com.tw/Attractions-g297907-Activities-Hualien_County.html")
        self.go_back(update)
    def on_enter_state109(self, update):
        update.message.reply_text("想要哪種種類呢？")
        update.message.reply_text("1.人文\n")
        photo=open('pic/71.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("2.自然\n")
        photo=open('pic/72.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("3.親子共遊\n")
        photo=open('pic/73.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()

###################################################################################################
    def on_enter_state110(self, update):
        update.message.reply_text("我推薦這個網址看看吧\nhttps://www.funtime.com.tw/blog/funtime/%E5%87%BA%E7%99%BC%E5%90%A7%EF%BC%81%E5%8F%B0%E6%9D%B1%E4%B8%8D%E8%83%BD%E9%8C%AF%E9%81%8E%E7%9A%8410%E5%A4%A7%E6%99%AF%E9%BB%9E\n")
        update.message.reply_text("http://travel178.blogspot.com/2012/09/Taitung-Day-Tour.html")
        self.go_back(update)
    def on_enter_state111(self, update):
        update.message.reply_text("想要哪種種類呢？")
        update.message.reply_text("1.人文\n")
        photo=open('pic/74.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("2.自然\n")
        photo=open('pic/75.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("3.親子共遊\n")
        photo=open('pic/76.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()

###################################################################################################
    def on_enter_state112(self, update):
        update.message.reply_text("查詢的結果：\n")
        photo=open('pic/71.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：松園別館\n地址：花蓮縣花蓮市松園街65號\n網路資訊：http://www.pinegarden.com.tw/\n")
        update.message.reply_text("想要更多旅遊地點,可以參考此網站：http://kenalice0110.pixnet.net/blog/post/43033907-%E3%80%90%E9%81%8A%E3%80%91%E6%87%B6%E4%BA%BA%E5%8C%85%EF%BC%9A26%E8%99%95%E8%8A%B1%E8%93%AE%E5%BF%85%E9%81%8A%E6%99%AF%E9%BB%9E%E6%8E%A8%E8%96%A6%282017.02\n")
        self.go_back(update)
    def on_enter_state113(self, update):
        update.message.reply_text("查詢的結果：\n")
        photo=open('pic/72.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：清水斷崖\n地址：花蓮縣秀林鄉\n網路資訊：http://www.taroko.gov.tw/zh-tw/Tourism/AttractionDetail?id=12\n")
        update.message.reply_text("想要更多旅遊地點,可以參考此網站：http://kenalice0110.pixnet.net/blog/post/43033907-%E3%80%90%E9%81%8A%E3%80%91%E6%87%B6%E4%BA%BA%E5%8C%85%EF%BC%9A26%E8%99%95%E8%8A%B1%E8%93%AE%E5%BF%85%E9%81%8A%E6%99%AF%E9%BB%9E%E6%8E%A8%E8%96%A6%282017.02\n")
        self.go_back(update)

    def on_enter_state114(self, update):
        update.message.reply_text("查詢的結果：\n")
        photo=open('pic/73.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：遠雄海洋公園\n地址：花蓮縣壽豐鄉鹽寮村福德189號\n網路資訊：http://www.farglory-oceanpark.com.tw/index.php?site=1\n")
        update.message.reply_text("想要更多旅遊地點,可以參考此網站：http://kenalice0110.pixnet.net/blog/post/43033907-%E3%80%90%E9%81%8A%E3%80%91%E6%87%B6%E4%BA%BA%E5%8C%85%EF%BC%9A26%E8%99%95%E8%8A%B1%E8%93%AE%E5%BF%85%E9%81%8A%E6%99%AF%E9%BB%9E%E6%8E%A8%E8%96%A6%282017.02\n")
        self.go_back(update)

####################################################################################################
    def on_enter_state115(self, update):
        update.message.reply_text("查詢的結果：\n")
        photo=open('pic/74.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：八仙洞遺址\n地址：台東縣長濱鄉三間村水母丁1-4號\n網路資訊：https://www.eastcoast-nsa.gov.tw/zh-tw/Attractions/Detail/37\n")
        update.message.reply_text("想要更多旅遊地點,可以參考此網站：https://www.tripadvisor.com.tw/Attractions-g304163-Activities-Taitung_County.html\n")
        self.go_back(update)
    def on_enter_state116(self, update):
        update.message.reply_text("查詢的結果：\n")
        photo=open('pic/75.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：蘭嶼\n地址：臺東縣蘭嶼鄉\n網路資訊：http://dailin114.pixnet.net/blog/post/42682181-%E5%8F%B0%E7%81%A3%E9%9B%A2%E5%B3%B6%E3%80%8B%E8%98%AD%E5%B6%BC%E9%81%8A%E8%A8%98-%EF%BC%8D-4%E5%A4%A92%E5%A4%9C%E6%87%B6%E4%BA%BA%E5%8C%85-%E8%8A%B1%E8%B2%BB%E9%A0%90\n")
        update.message.reply_text("想要更多旅遊地點,可以參考此網站：https://www.tripadvisor.com.tw/Attractions-g304163-Activities-Taitung_County.html\n")
        self.go_back(update)

    def on_enter_state117(self, update):
        update.message.reply_text("查詢的結果：\n")
        photo=open('pic/76.jpg','rb')
        update.message.reply_photo(photo)
        photo.close()
        update.message.reply_text("名稱：國立臺灣史前文化博物館\n地址：台東縣台東市博物館路1號\n網路資訊：http://www.nmp.gov.tw/\n")
        update.message.reply_text("想要更多旅遊地點,可以參考此網站：https://www.tripadvisor.com.tw/Attractions-g304163-Activities-Taitung_County.html\n")
        self.go_back(update)

####################################################################################################

    def on_exit_state1(self, update):
        print('Leaving state1')

    def on_exit_state2(self, update):
        print('Leaving state2')
