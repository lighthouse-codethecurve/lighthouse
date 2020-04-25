# -*- coding: utf-8 -*-
import requests
import re
import json
from requests.exceptions import RequestException
from multiprocessing import Pool
import pandas as pd
import numpy as np

#获取附加网址
r=set()
webitems=[]
labels=[]
ls=[]
items1=[]
items2=[]
items=[]
pattern = re.compile('<a tabindex="-1" aria-label=.*? class="_dsx40t2" href=\"(.*?)\">',re.S)
webitems = re.findall(pattern,'<ul class="_mhlvz8y" data-test-id="learn-menu"><li><div class="_135t03c"><h2 data-test-learn-menu-domain="math" class="_1gki889"><ul><li data-navigable-index="0"><a tabindex="-1" class="_78tn9w6" href="/math">Math</a></li></ul></h2><ul class="_haphvq"><li data-navigable-index="1"><a tabindex="-1" aria-label="Early math" class="_dsx40t2" href="/math/early-math"><span class="_138jip5">Early math</span></a></li><li data-navigable-index="2"><a tabindex="-1" aria-label="Arithmetic" class="_dsx40t2" href="/math/arithmetic"><span class="_138jip5">Arithmetic</span></a></li><li data-navigable-index="3"><a tabindex="-1" aria-label="Pre-algebra" class="_dsx40t2" href="/math/pre-algebra"><span class="_138jip5">Pre-algebra</span></a></li><li data-navigable-index="4"><a tabindex="-1" aria-label="Algebra 1" class="_dsx40t2" href="/math/algebra"><span class="_138jip5">Algebra 1</span></a></li><li data-navigable-index="5"><a tabindex="-1" aria-label="Geometry" class="_dsx40t2" href="/math/geometry"><span class="_138jip5">Geometry</span></a></li><li data-navigable-index="6"><a tabindex="-1" aria-label="Algebra 2" class="_dsx40t2" href="/math/algebra2"><span class="_138jip5">Algebra 2</span></a></li><li data-navigable-index="7"><a tabindex="-1" aria-label="Trigonometry" class="_dsx40t2" href="/math/trigonometry"><span class="_138jip5">Trigonometry</span></a></li><li data-navigable-index="8"><a tabindex="-1" aria-label="Precalculus" class="_dsx40t2" href="/math/precalculus"><span class="_138jip5">Precalculus</span></a></li><li data-navigable-index="9"><a tabindex="-1" aria-label="Statistics &amp; probability" class="_dsx40t2" href="/math/statistics-probability"><span class="_138jip5">Statistics &amp; probability</span></a></li><li data-navigable-index="10"><a tabindex="-1" aria-label="AP®︎ Calculus AB" class="_dsx40t2" href="/math/ap-calculus-ab"><span class="_138jip5">AP®︎ Calculus AB</span></a></li><li data-navigable-index="11"><a tabindex="-1" aria-label="AP®︎ Calculus BC" class="_dsx40t2" href="/math/ap-calculus-bc"><span class="_138jip5">AP®︎ Calculus BC</span></a></li><li data-navigable-index="12"><a tabindex="-1" aria-label="AP®︎ Statistics" class="_dsx40t2" href="/math/ap-statistics"><span class="_138jip5">AP®︎ Statistics</span></a></li><li data-navigable-index="13"><a tabindex="-1" aria-label="Multivariable calculus" class="_dsx40t2" href="/math/multivariable-calculus"><span class="_138jip5">Multivariable calculus</span></a></li><li data-navigable-index="14"><a tabindex="-1" aria-label="Differential equations" class="_dsx40t2" href="/math/differential-equations"><span class="_138jip5">Differential equations</span></a></li><li data-navigable-index="15"><a tabindex="-1" aria-label="Linear algebra" class="_dsx40t2" href="/math/linear-algebra"><span class="_138jip5">Linear algebra</span></a></li></ul></div></li><li><div class="_135t03c"><h2 data-test-learn-menu-domain="math" class="_1gki889"><ul><li data-navigable-index="16"><a tabindex="-1" class="_78tn9w6" href="/math/k-8-grades">Math by grade</a></li></ul></h2><ul class="_haphvq"><li data-navigable-index="17"><a tabindex="-1" aria-label="Preschool app" href="/kids" class="_dsx40t2"><span class="_138jip5">Preschool app</span></a></li><li data-navigable-index="18"><a tabindex="-1" aria-label="Kindergarten" class="_dsx40t2" href="/math/cc-kindergarten-math"><span class="_138jip5">Kindergarten</span></a></li><li data-navigable-index="19"><a tabindex="-1" aria-label="1st grade" class="_dsx40t2" href="/math/cc-1st-grade-math"><span class="_138jip5">1st grade</span></a></li><li data-navigable-index="20"><a tabindex="-1" aria-label="2nd grade" class="_dsx40t2" href="/math/cc-2nd-grade-math"><span class="_138jip5">2nd grade</span></a></li><li data-navigable-index="21"><a tabindex="-1" aria-label="3rd grade" class="_dsx40t2" href="/math/cc-third-grade-math"><span class="_138jip5">3rd grade</span></a></li><li data-navigable-index="22"><a tabindex="-1" aria-label="4th grade" class="_dsx40t2" href="/math/cc-fourth-grade-math"><span class="_138jip5">4th grade</span></a></li><li data-navigable-index="23"><a tabindex="-1" aria-label="5th grade" class="_dsx40t2" href="/math/cc-fifth-grade-math"><span class="_138jip5">5th grade</span></a></li><li data-navigable-index="24"><a tabindex="-1" aria-label="6th grade" class="_dsx40t2" href="/math/cc-sixth-grade-math"><span class="_138jip5">6th grade</span></a></li><li data-navigable-index="25"><a tabindex="-1" aria-label="7th grade" class="_dsx40t2" href="/math/cc-seventh-grade-math"><span class="_138jip5">7th grade</span></a></li><li data-navigable-index="26"><a tabindex="-1" aria-label="8th grade" class="_dsx40t2" href="/math/cc-eighth-grade-math"><span class="_138jip5">8th grade</span></a></li><li data-navigable-index="27"><a tabindex="-1" aria-label="Illustrative Mathematics" class="_dsx40t2" href="/math/illustrative-math"><span class="_138jip5">Illustrative Mathematics</span></a></li><li data-navigable-index="28"><a tabindex="-1" aria-label="Eureka Math/EngageNY" class="_dsx40t2" href="/math/engageny"><span class="_138jip5">Eureka Math/EngageNY</span></a></li><li data-navigable-index="29"><a tabindex="-1" aria-label="High school" class="_dsx40t2" href="/math/high-school-math"><span class="_138jip5">High school</span></a></li></ul></div></li><li><div class="_135t03c"><h2 data-test-learn-menu-domain="khan-for-educators" class="_1gki889"><ul><li data-navigable-index="30"><a tabindex="-1" class="_78tn9w6" href="/khan-for-educators/khan-kids-app-page">Khan Kids app (ages 2-7)</a></li></ul></h2><ul class="_haphvq"><li data-navigable-index="31"><a tabindex="-1" aria-label="Math, Reading &amp; Social Emotional Learning" href="/kids" class="_dsx40t2"><span class="_138jip5">Math, Reading &amp; Social Emotional Learning</span></a></li></ul></div></li><li><div class="_135t03c"><h2 data-test-learn-menu-domain="science" class="_1gki889"><ul><li data-navigable-index="32"><a tabindex="-1" class="_78tn9w6" href="/science">Science &amp; engineering</a></li></ul></h2><ul class="_haphvq"><li data-navigable-index="33"><a tabindex="-1" aria-label="Physics" class="_dsx40t2" href="/science/physics"><span class="_138jip5">Physics</span></a></li><li data-navigable-index="34"><a tabindex="-1" aria-label="AP®︎ Physics 1" class="_dsx40t2" href="/science/physics/ap-physics-1"><span class="_138jip5">AP®︎ Physics 1</span></a></li><li data-navigable-index="35"><a tabindex="-1" aria-label="AP®︎ Physics 2" class="_dsx40t2" href="/science/physics/ap-physics-2"><span class="_138jip5">AP®︎ Physics 2</span></a></li><li data-navigable-index="36"><a tabindex="-1" aria-label="Cosmology &amp; astronomy" class="_dsx40t2" href="/science/physics/cosmology-and-astronomy"><span class="_138jip5">Cosmology &amp; astronomy</span></a></li><li data-navigable-index="37"><a tabindex="-1" aria-label="Chemistry" class="_dsx40t2" href="/science/chemistry"><span class="_138jip5">Chemistry</span></a></li><li data-navigable-index="38"><a tabindex="-1" aria-label="AP®︎ Chemistry beta" class="_dsx40t2" href="/science/chemistry/ap-chemistry-beta"><span class="_138jip5">AP®︎ Chemistry beta</span></a></li><li data-navigable-index="39"><a tabindex="-1" aria-label="AP®︎ Chemistry" class="_dsx40t2" href="/science/chemistry/ap-chemistry"><span class="_138jip5">AP®︎ Chemistry</span></a></li><li data-navigable-index="40"><a tabindex="-1" aria-label="Organic chemistry" class="_dsx40t2" href="/science/organic-chemistry"><span class="_138jip5">Organic chemistry</span></a></li><li data-navigable-index="41"><a tabindex="-1" aria-label="Biology" class="_dsx40t2" href="/science/biology"><span class="_138jip5">Biology</span></a></li><li data-navigable-index="42"><a tabindex="-1" aria-label="High school biology" class="_dsx40t2" href="/science/high-school-biology"><span class="_138jip5">High school biology</span></a></li><li data-navigable-index="43"><a tabindex="-1" aria-label="AP®︎ Biology" class="_dsx40t2" href="/science/ap-biology"><span class="_138jip5">AP®︎ Biology</span></a></li><li data-navigable-index="44"><a tabindex="-1" aria-label="Health &amp; medicine" class="_dsx40t2" href="/science/health-and-medicine"><span class="_138jip5">Health &amp; medicine</span></a></li><li data-navigable-index="45"><a tabindex="-1" aria-label="Electrical engineering" class="_dsx40t2" href="/science/electrical-engineering"><span class="_138jip5">Electrical engineering</span></a></li></ul></div></li><li><div class="_135t03c"><h2 data-test-learn-menu-domain="computing" class="_1gki889"><ul><li data-navigable-index="46"><a tabindex="-1" class="_78tn9w6" href="/computing">Computing</a></li></ul></h2><ul class="_haphvq"><li data-navigable-index="47"><a tabindex="-1" aria-label="Computer programming" class="_dsx40t2" href="/computing/computer-programming"><span class="_138jip5">Computer programming</span></a></li><li data-navigable-index="48"><a tabindex="-1" aria-label="Computer science" class="_dsx40t2" href="/computing/computer-science"><span class="_138jip5">Computer science</span></a></li><li data-navigable-index="49"><a tabindex="-1" aria-label="AP®︎ Computer Science Principles" class="_dsx40t2" href="/computing/ap-computer-science-principles"><span class="_138jip5">AP®︎ Computer Science Principles</span></a></li><li data-navigable-index="50"><a tabindex="-1" aria-label="Hour of Code" class="_dsx40t2" href="/computing/hour-of-code"><span class="_138jip5">Hour of Code</span></a></li><li data-navigable-index="51"><a tabindex="-1" aria-label="Computer animation" class="_dsx40t2" href="/partner-content/pixar"><span class="_138jip5">Computer animation</span></a></li></ul></div></li><li><div class="_135t03c"><h2 data-test-learn-menu-domain="humanities" class="_1gki889"><ul><li data-navigable-index="52"><a tabindex="-1" class="_78tn9w6" href="/humanities">Arts &amp; humanities</a></li></ul></h2><ul class="_haphvq"><li data-navigable-index="53"><a tabindex="-1" aria-label="US history" class="_dsx40t2" href="/humanities/us-history"><span class="_138jip5">US history</span></a></li><li data-navigable-index="54"><a tabindex="-1" aria-label="AP®︎ US History" class="_dsx40t2" href="/humanities/us-history/ap-us-history"><span class="_138jip5">AP®︎ US History</span></a></li><li data-navigable-index="55"><a tabindex="-1" aria-label="World history" class="_dsx40t2" href="/humanities/world-history"><span class="_138jip5">World history</span></a></li><li data-navigable-index="56"><a tabindex="-1" aria-label="AP®︎ World History" class="_dsx40t2" href="/humanities/ap-world-history"><span class="_138jip5">AP®︎ World History</span></a></li><li data-navigable-index="57"><a tabindex="-1" aria-label="US government and civics" class="_dsx40t2" href="/humanities/us-government-and-civics"><span class="_138jip5">US government and civics</span></a></li><li data-navigable-index="58"><a tabindex="-1" aria-label="AP®︎ US Government &amp; Politics" class="_dsx40t2" href="/humanities/ap-us-government-and-politics"><span class="_138jip5">AP®︎ US Government &amp; Politics</span></a></li><li data-navigable-index="59"><a tabindex="-1" aria-label="Art history" class="_dsx40t2" href="/humanities/art-history"><span class="_138jip5">Art history</span></a></li><li data-navigable-index="60"><a tabindex="-1" aria-label="AP®︎ Art History" class="_dsx40t2" href="/humanities/ap-art-history"><span class="_138jip5">AP®︎ Art History</span></a></li><li data-navigable-index="61"><a tabindex="-1" aria-label="Grammar" class="_dsx40t2" href="/humanities/grammar"><span class="_138jip5">Grammar</span></a></li><li data-navigable-index="62"><a tabindex="-1" aria-label="Storytelling" class="_dsx40t2" href="/humanities/hass-storytelling"><span class="_138jip5">Storytelling</span></a></li></ul></div></li><li><div class="_135t03c"><h2 data-test-learn-menu-domain="economics-finance-domain" class="_1gki889"><ul><li data-navigable-index="63"><a tabindex="-1" class="_78tn9w6" href="/economics-finance-domain">Economics &amp; finance</a></li></ul></h2><ul class="_haphvq"><li data-navigable-index="64"><a tabindex="-1" aria-label="Macroeconomics" class="_dsx40t2" href="/economics-finance-domain/macroeconomics"><span class="_138jip5">Macroeconomics</span></a></li><li data-navigable-index="65"><a tabindex="-1" aria-label="AP®︎ Macroeconomics" class="_dsx40t2" href="/economics-finance-domain/ap-macroeconomics"><span class="_138jip5">AP®︎ Macroeconomics</span></a></li><li data-navigable-index="66"><a tabindex="-1" aria-label="Microeconomics" class="_dsx40t2" href="/economics-finance-domain/microeconomics"><span class="_138jip5">Microeconomics</span></a></li><li data-navigable-index="67"><a tabindex="-1" aria-label="AP®︎ Microeconomics" class="_dsx40t2" href="/economics-finance-domain/ap-microeconomics"><span class="_138jip5">AP®︎ Microeconomics</span></a></li><li data-navigable-index="68"><a tabindex="-1" aria-label="Finance &amp; capital markets" class="_dsx40t2" href="/economics-finance-domain/core-finance"><span class="_138jip5">Finance &amp; capital markets</span></a></li></ul></div></li><li><div class="_135t03c"><h2 data-test-learn-menu-domain="test-prep" class="_1gki889"><ul><li data-navigable-index="69"><a tabindex="-1" class="_78tn9w6" href="/test-prep">Test prep</a></li></ul></h2><ul class="_haphvq"><li data-navigable-index="70"><a tabindex="-1" aria-label="SAT" href="/sat" class="_dsx40t2"><span class="_138jip5">SAT</span></a></li><li data-navigable-index="71"><a tabindex="-1" aria-label="LSAT" href="/prep/lsat" class="_dsx40t2"><span class="_138jip5">LSAT</span></a></li><li data-navigable-index="72"><a tabindex="-1" aria-label="Praxis Core" href="/prep/praxis-core" class="_dsx40t2"><span class="_138jip5">Praxis Core</span></a></li><li data-navigable-index="73"><a tabindex="-1" aria-label="MCAT" class="_dsx40t2" href="/test-prep/mcat"><span class="_138jip5">MCAT</span></a></li><li data-navigable-index="74"><a tabindex="-1" aria-label="GMAT" class="_dsx40t2" href="/test-prep/gmat"><span class="_138jip5">GMAT</span></a></li><li data-navigable-index="75"><a tabindex="-1" aria-label="IIT JEE" class="_dsx40t2" href="/test-prep/iit-jee-subject"><span class="_138jip5">IIT JEE</span></a></li><li data-navigable-index="76"><a tabindex="-1" aria-label="NCLEX-RN" class="_dsx40t2" href="/test-prep/nclex-rn"><span class="_138jip5">NCLEX-RN</span></a></li></ul></div></li><li><div class="_135t03c"><h2 data-test-learn-menu-domain="college-careers-more" class="_1gki889"><ul><li data-navigable-index="77"><a tabindex="-1" class="_78tn9w6" href="/college-careers-more">College, careers, &amp; more</a></li></ul></h2><ul class="_haphvq"><li data-navigable-index="78"><a tabindex="-1" aria-label="College admissions" class="_dsx40t2" href="/college-admissions"><span class="_138jip5">College admissions</span></a></li><li data-navigable-index="79"><a tabindex="-1" aria-label="Careers" class="_dsx40t2" href="/college-careers-more/career-content"><span class="_138jip5">Careers</span></a></li><li data-navigable-index="80"><a tabindex="-1" aria-label="Personal finance" class="_dsx40t2" href="/college-careers-more/personal-finance"><span class="_138jip5">Personal finance</span></a></li><li data-navigable-index="81"><a tabindex="-1" aria-label="Entrepreneurship" class="_dsx40t2" href="/college-careers-more/entrepreneurship2"><span class="_138jip5">Entrepreneurship</span></a></li><li data-navigable-index="82"><a tabindex="-1" aria-label="Growth mindset" class="_dsx40t2" href="/partner-content/learnstorm-growth-mindset-activities-us"><span class="_138jip5">Growth mindset</span></a></li></ul></div></li></ul>')
labels=list(set('/'.join(webitems).split('/')))
labels.sort()
labels[0]='course'
labels.append('website')
ls.append(labels)

#获取页面
def get_one_page(url):
    try:
        response = requests.get(url)
        print('Request to ' + url)
        if response.status_code == 200:
            return response.content.decode("utf-8")
        return None
    except RequestException:
        return None

#获取需要的标题
def parse_one_page(html):
    #TODO: regex optimization
    pattern = re.compile(r'<a data-test-id="unit-header" class="_dwmetq" href="(.*?)"><h3 class="_k50sd54">(.*?)</h3></a>')
    items2 = re.findall(pattern,html)
    for item in items2:
        items.append(item[1])
        items1.append(item[0])
    return items

#写入文件（标题）
'''
def write_to_file(content):
    with open('imooc.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')
        f.close()
'''
#sheet1主程序，加标签
def main(page):
    url = 'https://www.khanacademy.org'+webitems[page]
    html = get_one_page(url)
    # parse_one_page(html)
    # print(html)
    try:
        for item in parse_one_page(html):
            if item in r:
                continue
            else:
                r.add(item)
                addls=[0]*(len(labels))
                addls[0]=item
                addls[-1]='https://www.khanacademy.org'+items1[items.index(item)]
                for j in webitems[page].split('/'):
                    if j!='':
                        addls[labels.index(j)]=1
                ls.append(addls)
    except:
        pass



if __name__ == '__main__':
    for i in range(len(webitems)):
        main(i)
    data=np.array(ls[1:])
    data_df=pd.DataFrame(data)
    data_df.columns = ls[0]
    writer = pd.ExcelWriter('Save_Excel_v2.xlsx')
    data_df.to_excel(writer,'page_1')
    writer.save()

    #sheet2主程序，分层级
    match={}
    for i in range(len(webitems)):
        trans=webitems[i].split('/')
        if trans[1] in match.keys():
            match[trans[1]]=match[trans[1]]+trans[2:]
        else:
            match[trans[1]]=trans[1:]
            
    data_df = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in match.items()]))
    #data_df.columns = ['main','secondary']
    data_df.to_excel(writer,'level')
    writer.save()

