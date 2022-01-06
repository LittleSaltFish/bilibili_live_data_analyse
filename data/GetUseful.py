import os

type1 = "_DeltaTime,_ExactTime,_Date,_color,_content,_name,_msg_type,"
type2 = "_DeltaTime,_ExactTime,_Date,_content_cmd,_content_data_anchor_info_uid,_content_data_anchor_info_uname,_content_data_anchor_info_uface,_content_data_pk_info,_content_data_anchor_lottery,_content_data_timestamp,_content_data_guard_level,_content_data_fans_medal_level,_content_data_msg,_content_data_paid,_content_data_price,_content_data_gift_num,_content_data_gift_name,_content_data_gift_id,_content_data_uface,_content_data_uname,_content_data_uid,_content_data_type,_msg_type,"

for curDir, dirs, files in os.walk("./data/OutPut/"):
    for tdir in dirs:
        print(tdir)
        # os.system(f"mkdir ./data/Useful/{tdir}")
        for curDir1, dirs1, files1 in os.walk(f"./data/OutPut/{tdir}"):
            for tfile in files1:
                print(tfile)
                with open(f"./data/OutPut/{tdir}/{tfile}", encoding="utf-8-sig") as f:
                    title = f.readline()
                    title = title.replace("\n", "")
                    if title == type1:
                        os.system(
                            f"cp ./data/OutPut/{tdir}/{tfile} ./data/Useful/{tdir}/danmu.csv")
                    elif title == type2:
                        os.system(
                            f"cp ./data/OutPut/{tdir}/{tfile} ./data/Useful/{tdir}/gift.csv")
