from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from instaUserinfo import username,password

class Instagram:
    def __init__(self,username,password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option("prefs",{"intl.accept_languages":"en,en_US"})
        
        self.browser = webdriver.Chrome("chromedriver.exe",chrome_options=self.browserProfile)
        self.username = username
        self.password = password
        # self.followers = []
    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login")
        time.sleep(4)
        username = self.browser.find_element(By.XPATH, "")
        password = self.browser.find_element(By.XPATH, "")
        button = self.browser.find_element(By.XPATH, "")
        username.send_keys(self.username)
        password.send_keys(self.password)
        button.send_keys(Keys.ENTER)
        time.sleep(8)
    
    def getFollowers(self,max):
        self.browser.get("https://www.instagram.com/") # Nick
        time.sleep(4)
        self.browser.find_element(By.XPATH, "").click()
        time.sleep(5)


        dialog = self.browser.find_element(By.CSS_SELECTOR, "")        
        followersCount = len(dialog.find_elements(By.CSS_SELECTOR, ""))
        print(f"First Count: {followersCount}")
        n = 20
        action = webdriver.ActionChains(self.browser)
        
        while followersCount < max:
            dialog.click()
            # action.send_keys(Keys.PAGE_DOWN)
            # self.browser.execute_script
            
            action.send_keys(Keys.TAB + Keys.TAB)
            action.send_keys(Keys.SPACE * n).perform()
            # action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(4)
            
            newCount = len(dialog.find_elements(By.CSS_SELECTOR, "m"))
            
            if followersCount != newCount:
                followersCount = newCount
                print(f"Second Count: {newCount} ")
                time.sleep(3)
                
            else:
                break

        followers = dialog.find_elements(By.CSS_SELECTOR, "")
        followerList = []
        i = 0
        for user in followers:
            i +=1
            if i == max:
                break
            link = user.find_element(By.CSS_SELECTOR,"a").get_attribute("href")
            followerList.append(link)

        with open("followers.txt","w",encoding="UTF-8") as file:
            for item in followerList:
                file.write(item + "\n")
                        
    def followerUser(self,username):
        self.browser.get("http://www.instagram.com/"+ username)
        time.sleep(4)
        followButton =  self.browser.find_element(By.TAG_NAME, "button")
        if followButton.text != "Takiptesin":
            followButton.click()      
            time.sleep(5)
            print(f"{username} User Followed.")
        else:
            print(f"{username} You Are Already Following User..")
    
    def unfollowUser(self,username):
        self.browser.get("http://www.instagram.com/"+ username)
        time.sleep(4)
        followButton =  self.browser.find_element(By.TAG_NAME, "button")
        if followButton.text == "following":
            followButton.click()
            time.sleep(5)
            confirmButton = self.browser.find_element(By.XPATH,(''))
            confirmButton.click()
            time.sleep(5)
        else:
            print("Zaten Takip Etmiyorsunuz")
            
insta = Instagram(username,password)
insta.signIn()
insta.getFollowers(50)
# print(len(insta.followers))
# print(insta.followers)
# list = ["cagritaner","huzunlubiirponcik2","regloloji"]
# for user in list:
#     insta.followerUser(user)
#     time.sleep(3)
# insta.followerUser("cagritaner")
# insta.unfollowUser("cagritaner")