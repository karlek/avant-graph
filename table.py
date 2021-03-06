from enum import Enum

class Val(object):
    def __init__(self, v, type):
        self.v    = v
        self.type = type

class Type(Enum):
    uni    = 1
    department = 2
    field  = 3

Table = {
    177:Val('KTH', Type.uni),

    5956:Val('Skolan för datavetenskap och kommunikation (CSC)', Type.department),
    5903:Val('Skolan för bioteknologi (BIO)', Type.department),
    6023:Val('Skolan för industriell teknik och management (ITM)', Type.department),
    5977:Val('Skolan för elektro- och systemteknik (EES)', Type.department),
    5994:Val('Skolan för informations- och kommunikationsteknik (ICT)', Type.department),
    5850:Val('Skolan för arkitektur och samhällsbyggnad (ABE)', Type.department),
    6172:Val('Skolan för teknikvetenskaplig kommunikation och lärande (ECE)', Type.department),
    6091:Val('Skolan för teknikvetenskap (SCI)', Type.department),
    5923:Val('Skolan för kemivetenskap (CHE)', Type.department),
    6161:Val('Skolan för teknik och hälsa (STH)', Type.department),

    # # # Red. Anm. duplicates???
    # 6215:Val('Mikroelektronik och informationsteknik, IMIT', Type.department),
    # 5995:Val('Mikroelektronik och informationsteknik, IMIT', Type.department),
    # # # SU..
    # 5999:Val('Data- och systemvetenskap, DSV', Type.department),
    # 6187:Val('Data- och systemvetenskap, DSV', Type.department),
    # 6159:Val('FaxénLaboratoriet', Type.department),
    # # # Dupes.
    # 6014:Val('Centra', Type.department),
    # 6147:Val('Centra', Type.department),
    # 6068:Val('Centra', Type.department),
    # 5968:Val('Centra', Type.department),
    # 6146:Val('Centra', Type.department),
    # 6169:Val('Centra', Type.department),
    # 5948:Val('Centra', Type.department),
    # 5990:Val('Centra', Type.department),
    # 5895:Val('Centra', Type.department),
    # 5914:Val('Centra', Type.department),
    # 12851:Val('Centra', Type.department),
    # 6019:Val('Electrumlaboratoriet, ELAB', Type.department),
    # 5921:Val('Science for Life Laboratory, SciLifeLab', Type.department),
    # 6018:Val('Zhejiang-KTH Joint Research Center of Photonics, JORCEP', Type.department),
    # 5996:Val('Mikroelektronik och tillämpad fysik, MAP', Type.department),
    # 5950:Val('Molekylär elektronik, CMD', Type.department),
    # 6217:Val('Numerisk analys och datalogi, NADA', Type.department),
    # 5957:Val('Numerisk Analys och Datalogi, NADA', Type.department),
    # # # Vettefan
    # 6038:Val('Maskinkonstruktion (Inst.)', Type.department),
    # 6044:Val('Maskinkonstruktion (Avd.)', Type.department),
    # # # http://rymd.lwr.kth.se/
    # # # 'Från och med den 25:e januari 2011 har vi en ny hemsida och sedan den 1:a juli 2013 är vi en avdelning vid Institutionen för hållbar utveckling, miljövetenskap och teknik: '
    # 5875:Val('Mark- och vattenteknik', Type.department),
    # 5997:Val('Elektronik- och datorsystem, ECS', Type.department),
    # # # Va i helvete
    # 6026:Val('Kraft- och värmeteknologi', Type.department),
    # 6030:Val('Industriell ekonomi och organisation (Inst.)', Type.department),
    # 6115:Val('Matematik (Inst.)', Type.department),
    # 6116:Val('Matematik (Avd.)', Type.department),
    # 5993:Val('ACCESS Linnaeus Centre', Type.department),
    # 5972:Val('Centre for Sustainable Communications, CESC', Type.department),
    # 6102:Val('MWL Marcus Wallenberg Laboratoriet', Type.department),
    # 6136:Val('Hållfasthetslära (Inst.)', Type.department),
    # 6137:Val('Hållfasthetslära (Avd.)', Type.department),
    # 6176:Val('Alfvénlaboratoriet', Type.department),
    # 5991:Val('Alfvénlaboratoriet', Type.department),
    # 6451:Val('Filosofi och teknikhistoria', Type.department),
    # 5964:Val('Tal, musik och hörsel, TMH', Type.department),
    # 5958:Val('Beräkningsbiologi, CB', Type.department),
    # 5961:Val('Medieteknik och grafisk produktion, Media (stängd 20111231)', Type.department),
    # 6155:Val('Linné Flow Center, FLOW', Type.department),
    # 6002:Val('Funktionella material, FNM (Stängd 20120101)', Type.department),
    # 5959:Val('Datorseende och robotik, CVAP', Type.department),
    # 6103:Val('MWL Strukturakustik', Type.department),
    # 5886:Val('Miljöstrategisk analys (flyttat 20130630)', Type.department),
    # 6207:Val('KTH Syd', Type.department),
    # 6001:Val('Materialfysik, MF (Stängd 20120101)', Type.department),
    # 10300:Val('Medieteknik och interaktionsdesign, MID', Type.department),
    # 11752:Val('Kvantelektronik och -optik, QEO', Type.department),
    # 13608:Val('SeRC - Swedish e-Science Research Centre ', Type.department),
    # 11800:Val('Numerisk analys, NA', Type.department),
    # 12850:Val('Nordic Institute for Theoretical Physics NORDITA', Type.department),
    # 12950:Val('High Performance Computing and Visualization (HPCViz)', Type.department),
    # 13056:Val('Optik och Fotonik, OFO', Type.department),
    # 13054:Val('Programvaruteknik och Datorsystem, SCS', Type.department),
    # 13302:Val('Funktionella material, FNM', Type.department),
    # 13303:Val('Halvledarmaterial, HMA', Type.department),
    # 13304:Val('Materialfysik, MF', Type.department),
    # 13606:Val('Miljöstrategisk analys (fms)', Type.department),
    # 13550:Val('Green Leap', Type.department),
    # 6028:Val('Energi och klimatstudier, ECS', Type.department),
    # 14950:Val('XPRES, Excellence in production research', Type.department),
    # 5963:Val('Teoretisk datalogi, TCS', Type.department),
    # 5969:Val('Centrum för Autonoma System, CAS', Type.department),
    # 5970:Val('Parallelldatorcentrum, PDC', Type.department),
    # 5896:Val('Centrum för bank och finans, Cefin', Type.department),
    # 6010:Val('Kommunikation: Infrastruktur och tjänster (Stängd 20120101)', Type.department),
    # 5898:Val('Centrum för studier inom vetenskap och innovation, CESIS (stängd 20110701)', Type.department),
    # 9301:Val('Centrum för studier inom vetenskap och innovation, CESIS', Type.department),
    # 5900:Val('Centrum för transportstudier, CTS', Type.department),
    # 6152:Val('Järnvägsgruppen, JVG', Type.department),
    # 874100:Val('Beräkningsvetenskap och beräkningsteknik (CST)', Type.department),
    # 873600:Val('Vägtekniks laboratorium', Type.department),
    # 7950:Val('Tillämpad maskinteknik (KTH Södertälje)', Type.department),
    # 6452:Val('Arkitekturskolan', Type.department),
    # 6104:Val('MWL Strömningsakustik', Type.department),
    # 5899:Val('Centrum för trafikforskning, CTR', Type.department),
    # 5992:Val('Centrum för elkraftteknik, EKC2', Type.department),
    # 5998:Val('Kommunikationssystem, CoS', Type.department),
    # 13052:Val('Optical Network Laboratory (ON Lab)', Type.department),
    # 6400:Val('Wireless at KTH', Type.department),
    # 6016:Val('KTH Center för Trådlösa System, Wireless@kth', Type.department),
    # 6017:Val('Kista Photonics Research Center, KPRC', Type.department),
    # # Tidigare insitutioner..?
    # 6175:Val('Tidigare Institutioner', Type.department),
    # 6206:Val('Kemiteknik', Type.department),
    # 6191:Val('Energiteknik', Type.department),
    # 6223:Val('Talöverföring och musikakustik', Type.department),
    # 6219:Val('Polymerteknologi', Type.department),
    # 6218:Val('Pappers- och massateknik', Type.department),
    # 6214:Val('Metallurgi', Type.department),
    # 6211:Val('Materialens processteknologi', Type.department),
    # 6220:Val('Produktionssystem', Type.department),
    # 6216:Val('Miljöskydd och arbetsvetenskap', Type.department),
    # 6201:Val('Industriell ekonomi och organisation', Type.department),
    # 6195:Val('Fiber- och polymerteknologi', Type.department),
    # 6193:Val('Farkostteknik', Type.department),
    # 6196:Val('Flygteknik', Type.department),
    # 6198:Val('Geodesi och fotogrammetri', Type.department),
    # 6199:Val('Halvledarlaboratoriet', Type.department),
    # 6181:Val('Biokemi och biokemisk teknologi', Type.department),
    # 6184:Val('Byggkonstruktion', Type.department),
    # 6185:Val('Byggnader och installationer', Type.department),
    # 6179:Val('Arkitektur och stadsbyggnad', Type.department),
    # 5974:Val('Centrum för användarorienterad IT-Design, CID', Type.department),
    # 5883:Val('Vattenförvaltning', Type.department),
    # 5918:Val('Albanova VinnExcellence Center for Protein Technology, ProNova', Type.department),
    # 6171:Val('Centrum för hälsa och byggande, CHB', Type.department),
    # 9850:Val('Data- och elektroteknik (Stängd 20130701)', Type.department),
    # 9852:Val('Naturvetenskapliga avdelningen (Stängd 20130701)', Type.department),
    # 9851:Val('Informatik, logistik och management (Stängd 20130701)', Type.department),
    # 6168:Val('Omgivningsfysiologi (Stängd 20130701)', Type.department),
    # 9303:Val('Medicinska sensorer, signaler och system (MSSS) (Stängd 20130701)', Type.department),
    # 6170:Val('Centrum för teknik, medicin och hälsa, CTMH', Type.department),
    # 5888:Val('Geoinformatik (stängd 20110301)', Type.department),
    # 6166:Val('Strukturell bioteknik (Stängd 20130701)', Type.department),
    # 6031:Val('Industriell dynamik (Stängd 20130101)', Type.department),
    # 6013:Val('Programvaru- och datorsystem, SCS (Stängd 20120101)', Type.department),
    # 6012:Val('Telekommunikationssystem, TSLab  (stängd 2012-01-01)', Type.department),
    # 6011:Val('Kommunikationssystem, CoS (stängd 2012-01-01)', Type.department),
    # 6007:Val('Kvantelektronik och -optik, QEO (flyttad till SCI 2011-07-01)', Type.department),
    # 6003:Val('Halvledarmaterial, HMA (Stängd 20120101)', Type.department),
    # 6163:Val('Strömnings- och klimatteknik (stängd 20090101)', Type.department),
    # 6160:Val('Centrum för förbränningsteknik, CICERO (stängd 20101231)', Type.department),
    # 6078:Val('Centrum för förbränningsteknik, CICERO (stängd 20101231)', Type.department),
    # 6037:Val('Genus, organisation och ledning (stängd 20130101)', Type.department),
    # 6033:Val('Industriell arbetsvetenskap (stängd 20130101)', Type.department),
    # 6032:Val('Industriell ekonomi och organisation (Avd.) (stängd 20130101)', Type.department),
    # 5962:Val('Numerisk analys, NA (stängd 2012-06-30)', Type.department),
    # 5960:Val('Människa-datorinteraktion, MDI (stängd 20111231)', Type.department),
    # 5893:Val('Trafik och Logistik (stängd 20110301)', Type.department),
    # 5892:Val('Transport och lokaliseringsanalys (stängd 20110301)', Type.department),
    # 5890:Val('Samhällsekonomi (stängd 20110301)', Type.department),
    # 6167:Val('Design, arbetsmiljö, säkerhet och hälsa, DASH', Type.department),
    # 6157:Val('VinnExcellence Center for ECO2 Vehicle design', Type.department),
    # 6156:Val('Strategiskt centrum för industriell och tillämpad matematik, CIAM', Type.department),
    # 6149:Val('Beräkningscentrum, KCSE', Type.department),
    # 6149:Val('Beräkningscentrum, KCSE', Type.department),
    # 6107:Val('MWL Vibrationsövervakning', Type.department),
    # 6106:Val('MWL Ultraljud', Type.department),
    # 6105:Val('MWL Numerisk akustik', Type.department),
    # 6087:Val('Centrum för leksaksforskning, SITREC', Type.department),
    # 6081:Val('KTH-centrum inom inbyggda system, ICES', Type.department),
    # 6080:Val('Design and Management of Manufacturing Systems, DMMS', Type.department),
    # 6070:Val('Brinell Center - Oorganiska gränsskikt, BRIIE', Type.department),
    # 10250:Val('Competence Center for Gas Exchange (CCGEx)', Type.department),
    # 6083:Val('VinnExcellence Center för Hierarkisk design av Industriella Material, HERO-M', Type.department),
    # 6021:Val('VinnExcellence Center for Intelligence in Paper and Packaging, iPACK', Type.department),
    # 5971:Val('Centrum för Talteknologi, CTT', Type.department),
    # 5954:Val('Wallenberg Wood Science Center', Type.department),
    # 5953:Val('Strategiskt Centrum för Biomimetiska Material, BioMime', Type.department),
    # 5952:Val('Centrum för Biofibermaterial, BiMaC', Type.department),
    # 5951:Val('Centrum för Industriell NMR-teknik', Type.department),
    # 5922:Val('Centrum för Bioprocessteknik, CBioPT', Type.department),
    # 5917:Val('Strategiskt Centrum för Biomimetiska Material, BioMime', Type.department),
    # 5882:Val('VA-teknik, Vatten, Avlopp och Avfall', Type.department),
    # 14362:Val('Centrum för flyg- och rymdfysiologi, SAPC', Type.department),
    # 13551:Val('Avdelningen för bibliotek, språk och ARC', Type.department),
    # 5975:Val('Parallel and Scientific Computing Institute, PSCI', Type.department),
    # 5920:Val('KTH-USTC Joint Center for Bio- and Nano-Materials', Type.department),
    # 5919:Val('KTH Genome Center', Type.department),
    # 13559:Val('Learning Lab IKT', Type.department),
    # 13053:Val('Radio Systems Laboratory (RS Lab)', Type.department),
    # 13051:Val('Network Systems Laboratory (NS Lab)', Type.department),
    # 13050:Val('Mobile Service Laboratory (MS Lab)', Type.department),

    13556:Val('Publiceringens infrastruktur', Type.field),
    10150:Val('Beräkningsbiofysik', Type.field),
    5965:Val('Språk och kommunikation', Type.field),
    5944:Val('Pappersteknologi', Type.field),
    6129:Val('Atom- och molekylfysik', Type.field),
    9854:Val('Språk och kommunikation', Type.field),
    14350:Val('Teknikdidaktik', Type.field),
    5947:Val('Träkemi och massateknologi', Type.field),
    5945:Val('Polymerteknologi', Type.field),
    5943:Val('Fiberteknologi', Type.field),
    6097:Val('Lättkonstruktioner', Type.field),
    6096:Val('Marina system', Type.field),
    6064:Val('Materialbearbetning', Type.field),
    6063:Val('Mätteknik och optik', Type.field),
    6062:Val('Datorsystem för konstruktion och tillverkning', Type.field),
    6059:Val('Mikro-modellering', Type.field),
    6058:Val('Mekanisk metallografi', Type.field),
    6057:Val('Materialteknologi', Type.field),
    6054:Val('Teknisk materialfysik ', Type.field),
    6052:Val('Termodynamisk modellering', Type.field),
    6051:Val('Keramteknologi', Type.field),
    6050:Val('Tillämpad processmetallurgi', Type.field),
    6047:Val('Tribologi', Type.field),
    6043:Val('Maskinelement', Type.field),
    6042:Val('Inbyggda styrsystem', Type.field),
    6041:Val('Mekatronik', Type.field),
    6040:Val('Förbränningsmotorteknik', Type.field),
    6039:Val('Integrerad produktutveckling', Type.field),
    6036:Val('Yrkeskunnande och teknologi', Type.field),
    6034:Val('Ekonomistyrning', Type.field),
    6027:Val('Uthålliga byggnadssystem', Type.field),
    6009:Val('Elektroniksystem', Type.field),
    5981:Val('Elektriska energisystem', Type.field),
    6046:Val('Produkt- och tjänstedesign', Type.field),
    5980:Val('Kommunikationsteori', Type.field),
    6045:Val('Produktinnovationsteknik', Type.field),
    5979:Val('Kommunikationsnät', Type.field),
    6095:Val('Flygdynamik', Type.field),
    6094:Val('Aeroakustik', Type.field),
    6093:Val('Aerodynamik', Type.field),
    6066:Val('Svetsteknologi', Type.field),
    6065:Val('Maskin- och processteknologi', Type.field),
    6127:Val('Biomekanik', Type.field),
    6125:Val('Turbulens', Type.field),
    6101:Val('Fordonsdynamik', Type.field),
    6123:Val('Teoretisk och tillämpad mekanik', Type.field),
    6122:Val('Processteknisk strömningsmekanik', Type.field),
    6120:Val('Strömningsfysik', Type.field),
    6117:Val('Matematisk statistik', Type.field),
    6114:Val('Kemisk fysik', Type.field),
    6144:Val('Materialteori', Type.field),
    6131:Val('Kärnfysik', Type.field),
    6132:Val('Kärnkraftssäkerhet', Type.field),
    10153:Val('Bro- och stålbyggnad', Type.field),
    10500:Val('Energisystemanalys', Type.field),
    11002:Val('Tillämpad fysikalisk kemi', Type.field),
    11801:Val('Mikro- och nanosystemteknik', Type.field),
    13000:Val('Material- och nanofysik', Type.field),
    13055:Val('Entreprenörskap och Innovation', Type.field),
    13300:Val('Industriell Management', Type.field),
    13301:Val('Organisation och ledning', Type.field),
    13600:Val('Industriell bioteknologi', Type.field),
    13601:Val('Proteinteknologi', Type.field),
    13602:Val('Proteomik och nanobioteknologi', Type.field),
    13603:Val('Flerskalig materialmodellering', Type.field),
    13604:Val('Hållbar utveckling, miljövetenskap och teknik', Type.field),
    13605:Val('Industriell ekologi', Type.field),
    13607:Val('Mark- och vattenteknik', Type.field),
    13609:Val('Metallernas gjutning', Type.field),
    14351:Val('Naturvetenskap och biomedicin', Type.field),
    14352:Val('Hälso- och systemvetenskap', Type.field),
    14353:Val('Grundläggande naturvetenskap', Type.field),
    14354:Val('Omgivningsfysiologi', Type.field),
    14355:Val('Strukturell bioteknik', Type.field),
    14356:Val('Medicinsk avbildning', Type.field),
    14357:Val('Neuronik', Type.field),
    14358:Val('Data- och elektroteknik', Type.field),
    14359:Val('Medicinska sensorer, signaler och system', Type.field),
    14360:Val('Ergonomi', Type.field),
    14361:Val('Systemsäkerhet och organisation', Type.field),
    14400:Val('Installations- och energisystem', Type.field),
    14550:Val('Vattendragsteknik', Type.field),
    14702:Val('Historiska studier av teknik, vetenskap och miljö', Type.field),
    15600:Val('Hållbarhet och industriell dynamik', Type.field),
    16000:Val('Medicinsk bildteknik', Type.field),
    17000:Val('Systemanalys och ekonomi', Type.field),
    17001:Val('Transportplanering, ekonomi och teknik', Type.field),
    17350:Val('Elektronik och Inbyggda System', Type.field),
    17351:Val('Industriell och Medicinsk Elektronik', Type.field),
    2229:Val('Teoretisk fysik', Type.field),
    4600:Val('Kommunikationssystem', Type.field),
    5851:Val('Arkitektur', Type.field),
    5852:Val('Arkitekturens historia och teori', Type.field),
    5853:Val('Arkitektonisk gestaltning', Type.field),
    5854:Val('Arkitekturteknik', Type.field),
    5855:Val('Kritiska studier i arkitektur', Type.field),
    5856:Val('Stadsbyggnad', Type.field),
    5857:Val('Byggvetenskap', Type.field),
    5858:Val('Installationsteknik', Type.field),
    5859:Val('Byggnadsteknik', Type.field),
    5860:Val('Byggnadsmaterial', Type.field),
    5861:Val('Betongbyggnad', Type.field),
    5862:Val('Miljö- och resursinformation', Type.field),
    5863:Val('Väg- och banteknik', Type.field),
    5864:Val('Jord- och bergmekanik', Type.field),
    5865:Val('Stålbyggnad', Type.field),
    5866:Val('Bro- och stålbyggnad', Type.field),
    5867:Val('Byggteknik och design', Type.field),
    5868:Val('Strömnings- och klimatteknik', Type.field),
    5869:Val('Fastigheter och byggande', Type.field),
    5870:Val('Bygg- och fastighetsekonomi', Type.field),
    5871:Val('Fastighetsvetenskap', Type.field),
    5872:Val('Projektkommunikation', Type.field),
    5873:Val('Teknik- och vetenskapshistoria', Type.field),
    5874:Val('Filosofi', Type.field),
    5876:Val('Teknisk geologi och geofysik', Type.field),
    5877:Val('Miljögeokemi och ekoteknik', Type.field),
    5878:Val('Miljöbedömning och -förvaltning', Type.field),
    5879:Val('Biogeofysik', Type.field),
    5880:Val('Vattenvårdsteknik', Type.field),
    5881:Val('Vattendragsteknik', Type.field),
    5884:Val('Samhällsplanering och miljö', Type.field),
    5885:Val('Urbana och regionala studier', Type.field),
    5889:Val('Transporter och samhällsekonomi', Type.field),
    5891:Val('Geodesi', Type.field),
    5894:Val('Säkerhetsforskning', Type.field),
    5904:Val('Miljömikrobiologi', Type.field),
    5905:Val('Biokemi', Type.field),
    5906:Val('Bioprocessteknik', Type.field),
    5907:Val('Genteknologi', Type.field),
    5908:Val('Molekylär Bioteknologi', Type.field),
    5909:Val('Nanobioteknologi', Type.field),
    5910:Val('Proteomik', Type.field),
    5911:Val('Teoretisk kemi', Type.field),
    5912:Val('Träbioteknik', Type.field),
    5913:Val('Glykovetenskap', Type.field),
    5924:Val('Kemi', Type.field),
    5925:Val('Analytisk kemi', Type.field),
    5926:Val('Oorganisk kemi', Type.field),
    5927:Val('Kärnkemi', Type.field),
    5928:Val('Organisk kemi', Type.field),
    5929:Val('Fysikalisk kemi', Type.field),
    5930:Val('Ytkemi', Type.field),
    5931:Val('Korrosionslära', Type.field),
    5932:Val('Yt- och korrosionsvetenskap', Type.field),
    5933:Val('Kemiteknik', Type.field),
    5934:Val('Tillämpad elektrokemi', Type.field),
    5935:Val('Kemisk apparatteknik', Type.field),
    5936:Val('Kemisk reaktionsteknik', Type.field),
    5937:Val('Kemisk teknologi', Type.field),
    5938:Val('Energiprocesser', Type.field),
    5939:Val('Teknisk strömningslära', Type.field),
    5940:Val('Fiber- och polymerteknik', Type.field),
    5941:Val('Biokompositer', Type.field),
    5942:Val('Ytbehandlingsteknik', Type.field),
    5946:Val('Polymera material', Type.field),
    5966:Val('Tal-kommunikation', Type.field),
    5967:Val('Musikakustik', Type.field),
    5978:Val('Reglerteknik', Type.field),
    5982:Val('Elektriska maskiner och effektelektronik', Type.field),
    5983:Val('Elektroteknisk teori och konstruktion', Type.field),
    5984:Val('Fusionsplasmafysik', Type.field),
    5985:Val('Industriella informations- och styrsystem', Type.field),
    5986:Val('Mikrosystemteknik', Type.field),
    5987:Val('Signalbehandling', Type.field),
    5988:Val('Rymd- och plasmafysik', Type.field),
    5989:Val('Ljud- och bildbehandling', Type.field),
    6000:Val('Materialfysik', Type.field),
    6004:Val('Fotonik och optik ', Type.field),
    6005:Val('Fotonik', Type.field),
    6006:Val('Optik', Type.field),
    6008:Val('Integrerade komponenter och kretsar', Type.field),
    6024:Val('Energiteknik', Type.field),
    6025:Val('Tillämpad termodynamik och kylteknik', Type.field),
    6029:Val('Industriell ekologi', Type.field),
    6048:Val('Materialvetenskap', Type.field),
    6049:Val('Tillämpad materialfysik', Type.field),
    6053:Val('Energi- och ugnsteknik', Type.field),
    6055:Val('Materialens processvetenskap', Type.field),
    6056:Val('Materialens processteknologi', Type.field),
    6060:Val('Metallografi', Type.field),
    6061:Val('Industriell produktion', Type.field),
    6067:Val('Lättkonstruktioner', Type.field),
    6092:Val('Farkost och flyg', Type.field),
    6098:Val('Järnvägsteknik', Type.field),
    6099:Val('Spårfordon', Type.field),
    6108:Val('Tillämpad fysik', Type.field),
    6109:Val('Biomedicinsk fysik och röntgenfysik', Type.field),
    6110:Val('Cellens fysik', Type.field),
    6111:Val('Experimentell biomolekylär fysik', Type.field),
    6112:Val('Laserfysik', Type.field),
    6113:Val('Nanostrukturfysik', Type.field),
    6118:Val('Optimeringslära och systemteori', Type.field),
    6119:Val('Mekanik', Type.field),
    6121:Val('Fysiokemisk strömningsmekanik', Type.field),
    6124:Val('Stabilitet, Transition, Kontroll', Type.field),
    6126:Val('Strukturmekanik', Type.field),
    6128:Val('Fysik', Type.field),
    6130:Val('Medicinsk avbildning', Type.field),
    6133:Val('Partikel- och astropartikelfysik', Type.field),
    6134:Val('Reaktorfysik', Type.field),
    6135:Val('Reaktorteknologi', Type.field),
    6138:Val('Biomekanik', Type.field),
    6139:Val('Teoretisk fysik', Type.field),
    6140:Val('Kondenserade materiens teori', Type.field),
    6141:Val('Statistisk fysik', Type.field),
    6142:Val('Matematisk fysik', Type.field),
    6143:Val('Teoretisk biologisk fysik', Type.field),
    6145:Val('Teoretisk partikelfysik', Type.field),
    6162:Val('Ergonomi', Type.field),
    6164:Val('Medicinsk teknik', Type.field),
    6165:Val('Neuronik', Type.field),
    6177:Val('Anläggning och miljö', Type.field),
    6178:Val('Arkitektur', Type.field),
    6182:Val('Bioteknologi', Type.field),
    6183:Val('Byggd miljö', Type.field),
    6186:Val('Byggvetenskap', Type.field),
    6188:Val('Elektronik', Type.field),
    6189:Val('Elektrotekniska system', Type.field),
    6190:Val('Elkraftteknik', Type.field),
    6192:Val('Farkost- och flygteknik', Type.field),
    6194:Val('Fastigheter och byggande', Type.field),
    6197:Val('Fysik', Type.field),
    6200:Val('Hållfasthetslära', Type.field),
    6202:Val('Industriell produktion', Type.field),
    6203:Val('Infrastruktur', Type.field),
    6204:Val('Infrastruktur och samhällsplanering', Type.field),
    6205:Val('Kemi', Type.field),
    6208:Val('Mark- och vattenteknik', Type.field),
    6209:Val('Maskinkonstruktion', Type.field),
    6210:Val('Matematik', Type.field),
    6212:Val('Materialvetenskap', Type.field),
    6213:Val('Mekanik', Type.field),
    6221:Val('Signaler, sensorer och system', Type.field),
    6222:Val('Tal, musik och hörsel', Type.field),
    6224:Val('Teknik- och vetenskapshistoria', Type.field),
    6225:Val('Teleinformatik', Type.field),
    6226:Val('Teoretisk elektroteknik', Type.field),
    6453:Val('Metallernas gjutning', Type.field),
    6454:Val('Tillämpad processmetallurgi', Type.field),
    6455:Val('Elektroniksystemkonstruktion', Type.field),
    7053:Val('Bank och finans', Type.field),
    7054:Val('Bebyggelseanalys', Type.field),
    7900:Val('Lärande', Type.field),
    7951:Val('Transportvetenskap', Type.field),
    7952:Val('Säkerhetsforskning', Type.field),
    7953:Val('Trafik och logistik', Type.field),
    7954:Val('Transport- och lokaliseringsanalys', Type.field),
    7955:Val('Väg- och banteknik', Type.field),
    7956:Val('Samhällsekonomi', Type.field),
    7957:Val('Geoinformatik och Geodesi', Type.field),
    8400:Val('Teoretisk kemi och biologi', Type.field),
    872750:Val('Geodesi och satellitpositionering', Type.field),
    872751:Val('Geoinformatik', Type.field),
    874000:Val('Medicinsk bildbehandling och visualisering', Type.field),
    874101:Val('Elkraftteknik', Type.field),
    9300:Val('Samhällsekonomi', Type.field),
    9302:Val('Elektrisk energiomvandling', Type.field),
    9500:Val('Affärsutveckling och Entreprenörskap', Type.field),
    9700:Val('Industriell marknadsföring', Type.field),
    9853:Val('Patientsäkerhet', Type.field),

    # Not KTH.
    # University. KTH, LTH, etc.
    # Red. anm. Helsinki University of Technology
    # 1751:Val('Tekniska Högskolan', Type.uni),
    # 118:Val('Tekniska Högskolan', Type.uni),
    # 101:Val('Högskolan i Jönköping', Type.uni),
    # 127:Val('Internationella Handelshögskolan', Type.uni),
    # 130:Val('IHH, Nationalekonomi', Type.uni),
    # 81:Val('Högskolan i Skövde', Type.uni),
    # 978:Val('Uppsala universitet', Type.uni),
    # 276:Val('Linköpings universitet', Type.uni),
    # 1800:Val('Hälsouniversitetet', Type.uni),
    # 7306:Val('Högskolan Dalarna', Type.uni),
    # 715:Val('Umeå universitet', Type.uni),
    #
    # 9051:Val('Science for Life Laboratory, SciLifeLab', Type.department),
    # 859:Val('Teknisk-naturvetenskapliga fakulteten', Type.department),
    # 870:Val('Institutionen för tillämpad fysik och elektronik', Type.department),
    # 85:Val('Institutionen för teknik och samhälle', Type.department),
    # 831:Val('Institutionen för informatik', Type.department),
    # 839:Val('Institutionen för informatik', Type.department),
    # 850:Val('Sociologiska institutionen', Type.department),
    # 866:Val('Institutionen för fysik', Type.department),
    # 869:Val('Institutionen för matematik och matematisk statistik', Type.department),
    # 6502:Val('Akademin för teknik och miljö', Type.department),
    # 9402:Val('Akademin Industri och samhälle', Type.department),
    #
    # 9451:Val('Energi och miljöteknik', Type.field),
    # 89:Val('Incitament nivå 3', Type.field),
    # 9439:Val('Byggteknik', Type.field),

    # Oanvända
    # 5977:Val('Skolan för elektro- och systemteknik (EES)', Type.department),
    # 6044:Val('Mark- och vattenteknik (flyttat 20130630)', Type.department),
    # 4200:Val('Östergötlands Läns Landsting', Type.department),
}
