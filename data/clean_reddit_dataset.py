import os

dir_path = './reddit_dataset/'
if not os.path.exists(dir_path):
    os.makedirs(dir_path)

raw_contents = [line.strip() for line in open('raw_reddit_data.csv', "r").readlines()]
for content in raw_contents:
    if content[0] != ',':
        content = content.lower().replace(" '", "'").replace(" n't", "n't").replace("&gt ; ","").replace(" ’ ", "'")

        if content[0] =='"':
            final_quote_index = content.rfind('"')
            text = content[1:final_quote_index]
            splitted_content = content[final_quote_index + 2:].split(",")

        else:
            splitted_content = content.split(",")
            text = splitted_content.pop(0)

        content_id = splitted_content[0]
        meta_label = splitted_content[2]
        sub_reddit = splitted_content[1]

        with open("{}{}_{}.txt".format(dir_path, meta_label, sub_reddit), "a+") as f:
            f.write("{}, {}\n".format(content_id, text))