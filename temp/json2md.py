#! /usr/bin/python

# 按目录层级输出 md 文件

import os,re,json

# 记录已经处理过的章节路径和标题
prev = {"path":"","title":""}

def build_index(file_path,chap_sec,chap_sec_name,comment):
    if not os.path.isfile(file_path):
        fp = open(file_path,'w')
        fp.write("---\n"
            + comment+ "bookCollapseSection: true\n"
            + "title: "+ chap_sec[chap_sec_name]+ "\n"
            + "weight: "+ chap_sec["weight"]+ "\n"
            + "bookHidden: true\n"
            + "prevPage: /docs"+ prev["path"]+ "\n"
            + "prevPageTitle: "+ prev["title"]+ "\n"
            + "nextPage: "+ "\n"
            + "nextPageTitle: "+ "\n"
            + "---\n\n"
            + "# "+ chap_sec[chap_sec_name]+ "\n\n")
        fp.close()

with open("./大纲.json",'r',encoding='utf-8') as fp:
    json_data = json.load(fp) # 载入 json 文档

    for chapter in json_data["chapters"]:
        
        # 新建各章目录
        chapter_dir= "./"+ chapter["chapNameE"]
        if not os.path.exists(chapter_dir):
            os.mkdir(chapter_dir)
        
        # 新建各章 _index.md 文件
        chapter_index= "./"+ chapter["chapNameE"]+ "/_index.md"
        build_index(chapter_index,chapter,"chapNameC","")

        # 记录路径和标题
        prev["path"] = "/"+ chapter["chapNameE"]
        prev["title"] = chapter["chapNameC"]
        
        for section in chapter["sections"]:
            # 新建各节目录
            section_dir= chapter_dir+ "/"+ section["secNameE"]
            if not os.path.exists(section_dir):
                os.mkdir(section_dir)
                
            # 新建各节 _index.md 文件
            section_index= section_dir+ "/_index.md"
            build_index(section_index,section,"secNameC","")

            # 记录路径和标题
            prev["path"] = "/"+ chapter["chapNameE"] + "/"+ section["secNameE"]
            prev["title"] = section["secNameC"]
            
            for subsection in section["subsections"]:
                # 新建各小节目录
                subsection_dir= section_dir+ "/"+ subsection["subsecNameE"]
                if not os.path.exists(subsection_dir):
                    os.mkdir(subsection_dir)
                    
                # 新建各小节 index.md 文件
                subsection_index= subsection_dir+ "/index.md"
                build_index(subsection_index,subsection,"subsecNameC","# ")

                # 记录路径和标题
                prev["path"] = "/"+ chapter["chapNameE"] \
                    + "/"+ section["secNameE"] \
                    + "/"+ subsection["subsecNameE"]
                prev["title"] = subsection["subsecNameC"]
