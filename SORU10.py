import re

tst_str = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur viverra tortor eu sagittis\
pellentesque. Pellentesque id ligula urna. Sed volutpat urna vitae urna malesuada dignissim. Nunc\
consequat dapibus consectetur. Curabitur pharetra ac dui eu luctus. Sed sit amet viverra libero.\
Quisque convallis gravida ex, nec molestie sapien commodo non."

for word in tst_str.split():
  if "o" in word:
    print (word.split(),end=",")