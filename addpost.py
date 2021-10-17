import sys
import os

def main():
  text=sys.argv[1]
  link=sys.argv[2]
  time=os.environ["POST_TIME"]
  new_post = "<div class=\"verticalLine dont-break-out\">\n <span style=\"font-size:10pt;display:inline-block;margin-left:10px\">\n"  + text +  "\n<a href=  \""   + link +   "\"  target=\"_blank\">\n"  + link +   "\n</a>  <br><span style=\"color:gray;font-size:9pt\">\n"  + time +  "\n</span>  </span>  </div> \n <br>\n"    
  new_post_lines = new_post.split("\n")
  tmp = open("tmp.txt", "a")

  for line in new_post_lines:
        tmp.write(line+"\n")

  f = open('posts.html',"r")
  old_post_lines = f.readlines()
  for line in old_post_lines:
        tmp.write(line)
  f.flush()
  f.close()
  tmp.close()
  os.system("mv tmp.txt posts.html")
  
if __name__ == "__main__":
  main()

