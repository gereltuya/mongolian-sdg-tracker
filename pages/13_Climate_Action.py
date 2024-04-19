import streamlit as st
import streamlit.components.v1 as components

def create_goal_section(number, goal, subdescription, iframe_url):
    st.markdown(f"### {number}. {goal}")
    st.markdown(f"_{subdescription}_")
    components.iframe(iframe_url, height=500)

st.title('Mongolian SDG Tracker төсөл: Зорилт #13 - ')
st.write('lorem ipsum dolor')

#JSON table
goals_data = [
  {
    "number": "13.1",
    "goal": "Улс орнуудад тулгарч буй цаг ууртай холбоотой аюул осол, байгалийн гамшгийг даван туулах, тэдгээрт зохицох чадавхыг бэхжүүлэх",
    "subgoals": [
      {
        "number": "13.1.1",
        "description": "100,000 хүнд ногдох гамшгийн улмаас амь насаа алдсан, сураггүй алга болсон болон гамшигт шууд нэрвэгдсэн хүний тоо",
        "iframe_url": "https://ourworldindata.org/grapher/deaths-and-missing-persons-due-to-natural-disasters"
      },
      {
        "number": "13.1.2",
        "description": "Гамшгийн эрсдэлийг бууруулах чиглэлээр 2015-2030 онд авч хэрэгжүүлэх Сендайн үйл ажиллагааны суурь баримт бичигтэй уялдуулсан гамшгийн эрсдэлийг бууруулах үндэсний стратегийг баталж, хэрэгжүүлдэг эсэх",
        "iframe_url": "https://ourworldindata.org/grapher/countries-with-legislative-regulatory-provisions-for-managing-disaster-risk"
      },
      {
        "number": "13.1.3",
        "description": "Гамшгийн эрсдэлийг бууруулах үндэсний стратегийн дагуу гамшгийн эрсдлийг бууруулах орон нутгийн стратегийг баталж, хэрэгжүүлдэг орон нутгийн засаг захиргааны эзлэх хувь",
        "iframe_url": "https://ourworldindata.org/grapher/local-govts-risk-reduction"
      }
    ]
  },
  {
    "number": "13.2",
    "goal": "Цаг уурын өөрчлөлтийн талаарх арга хэмжээг үндэсний бодлого, стратеги, төлөвлөлтөд тусгах",
    "subgoals": [
      {
        "number": "13.2.1",
        "description": "Хүнсний үйлдвэрлэлд саад болохгүйгээр хүлэмжийн хийн ялгарлыг бууруулахад чиглэсэн хөгжлийг дэмжих, уур амьсгалын өөрчлөлтийг даван туулах чадавхийг бий болгох, уур амьсгалын өөрчлөлтийн сөрөг нөлөөлөлд дасан зохицох чадварыг нэмэгдүүлэх талаар нэгдсэн бодлого, стратеги, төлөвлөгөөг бий болгон хэрэгжүүлж байгаагаа мэдээлж байгаа эсэх",
        "iframe_url": "https://ourworldindata.org/grapher/nationally-determined-contributions"
      },
      {
        "number": "13.2.2",
        "description": "Жилийн нийт хүлэмжийн хийн ялгаруулалт, тонноор",
        "iframe_url": "https://ourworldindata.org/grapher/total-ghg-emissions"
      }
    ]
  },
  {
    "number": "13.3",
    "goal": "Цаг уурын өөрчлөлтийг багасгах, цаг уурын өөрчлөлтөд дасан зохицох, цаг уурын өөрчлөлтийн нөлөөллийг бууруулах, урьдчилан сэрэмжлүүлэх талаарх ойлголт мэдлэгийг нэмэгдүүлж, хүмүүсийн болон институтийн чадавхыг сайжруулах",
    "subgoals": [
      {
        "number": "13.3.1",
        "description": "Бага, дунд, дээд боловсролын хөтөлбөртөө гамшгийг бууруулах, дасан зохицох, нөлөөллийг бууруулах, урьдчилан сэрэмжлүүлэх талаар тусгасан эсэх",
        "iframe_url": "https://ourworldindata.org/grapher/mainstreaming-sustainable-development-into-teacher-education"
      },
      {
        "number": "13.3.2",
        "description": "Уур амьсгалын өөрчлөлтөд дасан зохицох, түүнийг бууруулах, технологи дамжуулах, хөгжүүлэх үйл ажиллагааг нэвтрүүлэх чиглэлээр байгууллагын, системийн, хувь хүний чадавхийг бэхжүүлж байгаагаа мэдээлдэг эсэх"
      }
    ]
  },
  {
    "number": "13.a",
    "goal": "Эрсдэлийг бууруулах үндсэн арга хэмжээ болон түүний хэрэгжилтийн талаарх ил тод байдлын хүрээнд хөгжиж буй орнуудын хэрэгцээ шаардлагыг хангах, Ногоон цаг уурын сангийн үйл ажиллагааг тус санд хуримтлагдсан хөрөнгийг ашиглан аль болох хурдан бүрэн эхлүүлэх зорилгоор бүх төрлийн эх үүсвэрээс 2020 он гэхэд жил бүр 100 тэрбум ам.долларыг хамтран бүрдүүлэх зорилтын үүднээс НҮБ-ын Уур амьсгалын өөрчлөлтийн суурь конвенцийг хэрэгжүүлэхээр хүлээсэн хөгжингүй улс орнуудын үүрэг амлалтыг биелүүлэх",
    "subgoals": [
      {
        "number": "13.a.1",
        "description": "2020 оноос 2025 он хүртэл 100 тэрбум ам.долларыг бүрдүүлэх үүрэг амлалтыг биелүүлэхээр жил бүр бүрдүүлсэн хөрөнгийн хэмжээ, ам.доллараар",
        "iframe_url": "https://ourworldindata.org/grapher/green-climate-gcf-fund-pledges"
      }
    ]
  },
  {
    "number": "13.b",
    "goal": "Эмэгтэйчүүд, залуучууд, орон нутгийн болон эмзэг бүлгийн иргэдэд голлон анхаарч нэн буурай хөгжилтэй улс орнуудад цаг уурын өөрчлөлттэй холбоотой үр дүнтэй төлөвлөлт, менежмент хийх чадавхыг нэмэгдүүлэх механизмыг хөхүүлэн дэмжих",
    "subgoals": [
      {
        "number": "13.b.1",
        "description": "Эмэгтэйчүүд, залуучууд, орон нутгийн болон эмзэг бүлгийн иргэдэд чиглэсэн үр дүнтэй, уур амьсгалын өөрчлөлттэй холбоотой төлөвлөлт, удирдлагын чадавхыг дээшлүүлэх механизмыг бий болгоход мэргэжлийн дэмжлэг авч байгаа эсэх"
      }
    ]
  }
]

 

def create_goal_section(number, goal, subgoals):
    st.markdown(f"### {number}. {goal}")
    for subgoal in subgoals:
        st.markdown(f"_{subgoal['number']}. {subgoal['description']}_")
        if 'iframe_url' in subgoal:
            components.iframe(subgoal['iframe_url'], height=500)
        else:
            st.markdown("⚠️ Not available ⚠️")

for data in goals_data:
    create_goal_section(
        number=data["number"],
        goal=data["goal"],
        subgoals=data["subgoals"]
    )