import pickle
import streamlit as st
import pandas as pd

model = pickle.load(open('prediksi_ph.sav','rb'))

st.title('Prediksi pH')

df1 = pd.read_csv('airnov.csv', sep=';')

def show_deskripsi():
    st.write("Selamat datang di aplikasi prediksi ph berbasis web.")
    st.write("<div style='text-align: justify;'>Aplikasi ini menggunakan teknologi <i>Machine Learning</i> untuk memberikan prediksi yang akurat terkait tingkat pH air berdasarkan beberapa variabel kunci. Dengan memasukkan nilai-nilai seperti Hardness, Alkalinity, Carbonate Root, Nitrate, Nitrite, Free clorine, Total Clorine, Dissolved Oxygen, Temperature, dan pH,  pengguna dapat dengan mudah mendapatkan perkiraan tingkat keasaman atau alkalinitas air. Model <i>Machine Learning</i> yang kuat di balik aplikasi ini telah dilatih menggunakan data historis yang luas, memungkinkan sistem memberikan prediksi yang andal. Aplikasi ini dirancang untuk membantu pengguna dalam memantau kualitas air secara efisien, mengidentifikasi potensi ketidakseimbangan pH, dan memastikan air memenuhi standar kualitas yang aman. Sederhana, responsif, dan mudah digunakan, aplikasi ini menjadi alat yang ideal untuk pengelolaan dan analisis kualitas air.</div>", unsafe_allow_html=True)
    st.write("Dibuat oleh Risma Manura - 223307022")

def show_dataset():
    st.header("Dataset")
    st.dataframe(df1)
    st.markdown("""
( 1 ) **Hardness (Kekerasan Air)**
    - Hardness mengukur jumlah ion kalsium (Ca²⁺) dan magnesium (Mg²⁺) dalam air.
    - Nilai tinggi menunjukkan kandungan mineral tinggi, sementara nilai rendah menunjukkan air lembut.
    \n(
2 ) **Alkalinity (Alkalinitas)**
    - Kemampuan air untuk menetralkan asam, biasanya diukur sebagai kandungan ion karbonat (CO₃²⁻), bikarbonat (HCO₃⁻), dan hidroksida (OH⁻).
    - Alkalinitas tinggi biasanya berasal dari proses geologi seperti pelarutan batuan kapur.
    \n(
3 ) **Carbonate Root (Akar Karbonat)**
    - Ion karbonat (CO₃²⁻) merupakan komponen utama alkalinitas yang membantu menetralkan asam.
    - Nilai tinggi umumnya terjadi di daerah dengan batuan karbonat atau kapur.
    \n(
4 ) **Nitrate (Nitrat)**
    - Nitrat (NO₃⁻) adalah senyawa nitrogen yang sering ditemukan dalam air akibat pupuk pertanian, limbah hewan, atau peluruhan bahan organik.
    - Tingkat tinggi dapat menandakan polusi dari aktivitas manusia.
    \n(
5 ) **Nitrite (Nitrit)**
    - Nitrit (NO₂⁻) adalah produk antara dari konversi amonia menjadi nitrat.
    - Nitrit tinggi dalam air minum dapat mengindikasikan pencemaran bakteri atau pengolahan air yang buruk.
    \n(
6 ) **Free Chlorine (Klorin Bebas)**
    - Jumlah klorin bebas yang tersedia untuk mendisinfeksi air dari patogen.
    - Klorin berlebih dapat memberikan rasa atau bau yang tidak enak.
    \n(
7 ) **Total Chlorine (Total Klorin)**
    - Gabungan klorin bebas dan klorin terikat (seperti chloramines).
    - Nilai yang terlalu rendah menandakan risiko kontaminasi mikroba, sementara nilai tinggi dapat menyebabkan efek samping kesehatan.
    \n(
8 ) **Dissolved Oxygen (DO)**
    - Jumlah oksigen terlarut dalam air, penting untuk kehidupan akuatik.
    - Nilai tinggi menunjukkan kualitas air yang baik untuk ekosistem akuatik.
    \n(
9 ) **Temperature (Suhu)**
    - Mengacu pada suhu air.
    - Suhu tinggi dapat mengurangi kadar oksigen, sementara suhu rendah meningkatkan kapasitas air untuk melarutkan gas.
    \n(
10 ) **pH**
    - Mengukur tingkat keasaman atau alkalinitas air (skala 0-14).
    - pH yang tidak sesuai dapat merusak pipa, memengaruhi rasa, atau membahayakan kesehatan manusia dan makhluk hidup.
""")

def show_grafik():
    st.header("Grafik")

    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10 = st.tabs(["Hardness", "Alkalinity", "Carbonate Root", "Nitrate", "Nitrite", "Free Chlorine", "Total Chlorine", "Dissolved Oxygen", "Temperature", "pH"])

    with tab1:
        st.write("Grafik Hardness (Kekerasan Air)")
        chart_hardness = pd.DataFrame(df1, columns=["Hardness"])
        st.line_chart(chart_hardness)
    with tab2:
        st.write("Grafik Alkalinity (Alkalinitas)")
        chart_alkalinity = pd.DataFrame(df1, columns=["Alkalinity"])
        st.line_chart(chart_alkalinity)
    with tab3:
        st.write("Grafik Carbonate Root (Akar Karbonat)")
        chart_carbonateroot = pd.DataFrame(df1, columns=["Carbonate Root"])
        st.line_chart(chart_carbonateroot)
    with tab4:
        st.write("Grafik Nitrate (Nitrat)")
        chart_nitrate = pd.DataFrame(df1, columns=["Nitrate"])
        st.line_chart(chart_nitrate)
    with tab5:
        st.write("Grafik Nitrite (Nitrit)")
        chart_nitrite = pd.DataFrame(df1, columns=["Nitrite"])
        st.line_chart(chart_nitrite)
    with tab6:
        st.write("Grafik Free Chlorine (Klorin Bebas)")
        chart_freechlorine = pd.DataFrame(df1, columns=["Free Chlorine"])
        st.line_chart(chart_freechlorine)
    with tab7:
        st.write("Grafik Total Chlorine (Total Klorin)")
        chart_totalchlorine = pd.DataFrame(df1, columns=["Total Chlorine"])
        st.line_chart(chart_totalchlorine)
    with tab8:
        st.write("Grafik Dissolved Oxygen (DO)")
        chart_dissolvedoxygen = pd.DataFrame(df1, columns=["Dissolved Oxygen"])
        st.line_chart(chart_dissolvedoxygen)
    with tab9:
        st.write("Grafik Temperature (Suhu)")
        chart_temperature = pd.DataFrame(df1, columns=["Temperature"])
        st.line_chart(chart_temperature)
    with tab10:
        st.write("Grafik pH")
        chart_ph = pd.DataFrame(df1, columns=["pH"])
        st.line_chart(chart_ph)
    


def show_prediksi():
    st.header("Prediksi")
    st.write("Tentukan nilai-nilai pada variabel berikut untuk menentukan jenis kegagalan yang dialami oleh mesin:")
    Hardness = st.number_input('Input Hardness')
    Alkalinity = st.number_input('Input Alkalinity')
    CarbonateRoot = st.number_input('Input Carbonate Root')
    Nitrate = st.number_input('Input Nitrate')
    Nitrite	= st.number_input('Input Nitrite')
    Freeclorine = st.number_input('Input Free clorine')
    Temperature = st.number_input('Input Temperature')
    DissolvedOxygen = st.number_input('Input Dissolved Oxygen')

    predict = ''

    if st.button('Prediksi pH'):
    
        predict = model.predict([[Hardness, Alkalinity, CarbonateRoot, Nitrate, Nitrite, Freeclorine, Temperature, DissolvedOxygen]])
        st.write('Prediksi pH:', predict)

add_selectbox = st.sidebar.selectbox(
    "PILIH MENU",
    ("Deskripsi", "Dataset", "Grafik", "Prediksi")
)

if add_selectbox == "Deskripsi":
    show_deskripsi()
elif add_selectbox == "Dataset":
    show_dataset()
elif add_selectbox == "Grafik":
    show_grafik()
elif add_selectbox == "Prediksi":
    show_prediksi()