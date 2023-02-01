import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from numpy import array


if __name__ == "__main__":

    FRONT = np.array(
        [
            array([141.28121643, 75.85871696, 87.13249741]),
            array([94.1278038, 59.78442879, 90.57937927]),
            array([140.66949768, 44.52680626, 89.16461105]),
            array([92.87926331, 58.88413239, 92.90675125]),
            array([144.0053421, 72.5598381, 86.66637497]),
            array([93.86596756, 59.42230186, 90.96019058]),
            array([137.75837097, 86.5308754, 87.86659622]),
            array([96.64025879, 58.55225639, 89.91061935]),
            array([228.91086578, 164.25192566, -17.7392457]),
            array([142.76013031, 253.99675598, 9.02469935]),
            array([125.66215439, 48.87985134, 90.09341354]),
            array([134.74066849, 258.65109406, 6.95620009]),
            array([96.73936539, 58.59059448, 89.64583282]),
            array([144.31295013, 247.2650238, 9.79547622]),
            array([145.08704987, 244.00995178, 6.66132894]),
            array([98.37779617, 57.68398743, 89.79459381]),
            array([138.11986542, 65.97145805, 89.57698669]),
            array([173.13210602, 85.47419815, 82.39305954]),
            array([169.57218323, 86.36636658, 82.95272369]),
            array([134.63701019, 161.60601044, 69.38756104]),
            array([159.27921753, 76.05680237, 84.76862946]),
            array([166.84297791, 83.80194931, 84.30366821]),
            array([137.02050171, 157.22131805, 62.04100342]),
            array([186.33513489, 99.46493683, 80.89183655]),
            array([186.0373291, 93.98920975, 82.15478287]),
            array([233.18285522, 162.54257813, -19.11167469]),
            array([186.6046463, 87.55945587, 82.11798401]),
            array([238.43552551, 159.40062866, -21.95485268]),
            array([134.86150055, 272.25590515, 0.94816487]),
            array([182.44815979, 87.46429825, 82.23624878]),
            array([133.19006119, 152.71426086, 75.41493835]),
            array([240.61662445, 154.78787231, -25.26862164]),
            array([140.22064896, 154.78198471, 72.64367561]),
            array([255.47138519, 66.6760273, 14.19029951]),
            array([241.31199341, 155.68202667, -29.13704662]),
            array([238.32718506, 161.57303162, -28.12786903]),
            array([136.4008667, 270.69374084, -4.17020256]),
            array([141.43394318, 267.06439209, 1.17534733]),
            array([154.54684143, 38.12256393, 86.12095261]),
            array([240.2071579, 124.78021698, 21.49565449]),
            array([136.13367462, 271.55075378, -7.09802988]),
            array([144.94347687, 34.03052139, 87.08223038]),
            array([242.71295776, 109.02166443, 20.81952953]),
            array([247.56295929, 107.47159271, 19.53104477]),
            array([223.51307068, 89.52256088, 77.63249054]),
            array([248.38175812, 104.7731514, 16.60022831]),
            array([110.16636581, 46.45655174, 95.54735641]),
            array([151.17498932, 266.05990601, -4.40004528]),
            array([106.96899872, 50.32868385, 95.38826294]),
            array([135.58585663, 273.6592926, -6.71086114]),
            array([222.94777222, 95.7776268, 77.6772438]),
            array([108.719561, 48.3731987, 95.57818375]),
            array([214.67985687, 86.65221252, 78.71041489]),
            array([116.9591568, 37.55522461, 95.36120529]),
            array([116.72890091, 37.66851158, 95.48792953]),
            array([116.6318161, 152.19316864, 85.91438217]),
            array([107.55168381, 48.91085205, 95.9761055]),
            array([127.13998108, 279.47349243, -7.57319915]),
            array([128.52244415, -10.26622139, 94.50933228]),
            array([128.0335701, 279.15090637, -9.2023773]),
            array([199.58942566, 60.75095177, 79.86098022]),
            array([126.32388153, 4.46481482, 95.23689957]),
            array([187.24779053, 45.61036377, 81.78859253]),
            array([121.12146301, 23.85464878, 95.0571991]),
            array([178.84472198, 36.64794998, 83.72228851]),
            array([123.27486038, 13.55307965, 94.4596962]),
            array([226.26786804, 182.30354156, -10.49878721]),
            array([130.60888519, 288.24678955, -20.67480927]),
            array([224.20926361, 183.49498596, -9.33780112]),
            array([125.01322021, 289.82848206, -23.81225567]),
            array([224.06430511, 188.31486206, -9.65058169]),
            array([176.19102325, 35.30123482, 85.07210922]),
            array([223.48609467, 187.8385498, -5.67328104]),
            array([203.09024048, 55.09804153, 80.07868347]),
            array([222.66396484, 190.21876373, -6.36237295]),
            array([242.62404633, 84.72056122, 72.94024048]),
            array([226.99720764, 187.83413239, -13.47450728]),
            array([242.06701508, 88.19620361, 74.83140564]),
            array([228.37890625, 180.82763977, -17.01762476]),
            array([229.25753632, 183.94319611, -19.08524933]),
            array([246.79576416, 71.67297821, 72.19691544]),
            array([246.1851059, 71.9811142, 72.05829773]),
            array([120.70127869, 155.09269257, 84.91655884]),
            array([127.1123703, -6.50838575, 93.34151917]),
            array([121.92786102, 281.85727844, -7.5178544]),
            array([117.10619431, 161.18704529, 84.59906158]),
            array([125.03801422, 281.48772583, -8.4516088]),
            array([124.58824539, 12.40312745, 94.51311035]),
            array([125.1573822, 12.52760813, 94.39336624]),
            array([219.24061279, 192.21412048, -3.90631304]),
            array([222.2799057, 188.75903625, -5.05793171]),
            array([121.95151672, 280.94236145, -0.3079376]),
            array([229.28086243, 53.79823074, 77.37480774]),
            array([1.25695783e02, 2.76017920e02, 1.54538846e-01]),
            array([124.19275131, 276.20055542, -3.04666889]),
            array([134.32196198, 5.45748596, 90.73067398]),
            array([122.16365204, 279.06564026, -4.38116797]),
            array([110.92719421, 140.14992447, 86.40884933]),
            array([117.05851517, 281.94189148, -6.80723338]),
            array([116.15941238, 158.4405899, 85.48306885]),
            array([126.68469162, -1.70748214, 94.52148438]),
            array([123.83409042, 5.96405019, 94.8047348]),
            array([133.51651382, 275.6759613, -3.68068485]),
            array([132.61767349, 277.40517883, -4.07850294]),
            array([133.1233017, 186.75866241, 81.45771179]),
            array([218.35480652, 205.10618896, -0.6821475]),
            array([210.50325317, 210.75863647, 1.29450399]),
            array([115.97056427, 159.59922791, 84.70642548]),
            array([211.41850128, 207.75689545, -1.60607447]),
            array([148.44092026, 267.51441956, -5.43510756]),
            array([124.47202682, 188.20454254, 84.14450455]),
            array([126.08707352, 195.86031189, 81.83310318]),
            array([125.3337204, 189.21971436, 82.56176453]),
            array([218.03105316, 196.26829987, 6.07774415]),
            array([150.4935318, 266.97385864, 3.46185274]),
            array([121.44572525, 201.36133423, 83.2675354]),
            array([237.93636322, 85.46080551, 75.10180359]),
            array([119.47896729, 210.42014008, 81.60042114]),
            array([244.07890778, 79.32407532, 75.28586273]),
            array([242.53465729, 78.12946777, 75.7908783]),
            array([244.66184235, 76.65998306, 74.20601273]),
            array([147.51732864, 181.87325287, 61.2641571]),
            array([248.31466522, 125.27240982, 16.10027981]),
            array([127.3327034, 285.82513428, -13.45175261]),
            array([177.59959259, 34.28088017, 84.80434875]),
            array([184.45322571, 45.49687138, 83.71079407]),
            array([224.47574005, 105.98982849, 69.58171158]),
            array([224.02323151, 116.24840469, 69.12596283]),
            array([230.5409729, 113.96719284, 67.91816406]),
            array([232.76838837, 110.96502457, 68.40466309]),
            array([225.14042511, 182.57279358, 0.62157197]),
            array([231.48450623, 105.39269485, 69.83014679]),
            array([235.60485992, 94.99149628, 70.61265869]),
            array([227.92559967, 79.516539, 77.49395142]),
            array([228.69182281, 80.19804916, 77.39275055]),
            array([235.78598785, 67.75787354, 76.77534027]),
            array([121.64212875, 36.38587513, 93.82173767]),
            array([234.04015808, 71.20895538, 76.22236023]),
            array([122.24573135, 36.54232388, 93.77015228]),
            array([233.91546631, 70.50434532, 76.24671555]),
            array([127.56944885, 33.55152016, 92.59557037]),
            array([119.09690247, 297.56751709, -17.47854805]),
            array([129.21598816, 32.39647732, 90.51138611]),
            array([117.49955902, 286.05259094, -17.1690316]),
            array([195.05979767, 60.53797264, 81.16635361]),
            array([216.09499969, 72.87233505, 78.51989059]),
            array([219.88833313, 208.35366058, -16.76516819]),
            array([112.68787842, 290.94736938, -7.65360883]),
            array([131.67335129, 8.53663044, 93.0774559]),
            array([219.80629578, 205.0206604, -12.44233556]),
            array([145.12098999, 40.67853928, 86.99792862]),
            array([130.39726562, 7.2177701, 93.14079971]),
            array([217.26742859, 205.41443634, -12.51341133]),
            array([127.15537033, 209.21745148, 78.610186]),
            array([133.18199768, 27.97651691, 92.00757904]),
            array([219.9942688, 204.94876709, -15.1078845]),
            array([124.79931412, 214.69122162, 77.68812714]),
            array([214.48580475, 207.32175446, -12.05720284]),
            array([129.39822922, 212.3514267, 74.41741028]),
            array([213.87010803, 207.63545837, -16.39869375]),
            array([203.98136139, 39.82007256, 81.5749794]),
            array([211.76380463, 208.65421448, -17.33609667]),
            array([211.13041992, 51.71580276, 79.92367096]),
            array([128.82754669, 209.88496094, 76.61032104]),
            array([138.82126007, 281.82266235, -9.49000573]),
            array([245.07418671, 84.59634323, 72.24849625]),
            array([128.28109283, 208.43053894, 78.19627914]),
            array([140.92587967, 285.74880066, -9.72449164]),
            array([242.04122467, 91.19630966, 72.1692543]),
            array([102.43309097, 54.94695854, 96.28633118]),
            array([243.88187408, 86.41464386, 71.65683899]),
            array([100.04586105, 55.27334404, 96.12405472]),
            array([99.11143646, 55.47903519, 95.56827087]),
            array([256.42516632, 117.07596588, 10.75181646]),
            array([256.39883423, 121.67161255, 10.59205847]),
            array([102.99434738, 53.05345039, 96.01969681]),
            array([257.5363327, 119.60458832, 10.1718514]),
            array([125.4772583, 302.20304871, -24.19275417]),
            array([104.4742981, 52.90350952, 96.51628342]),
            array([258.51929626, 115.21054459, 9.42445922]),
            array([122.33334656, 297.64147644, -23.11940422]),
            array([254.81034241, 130.4129837, 14.95459661]),
            array([122.04328918, 298.27225647, -22.45928802]),
            array([98.5955162, 57.06432381, 97.14272766]),
            array([2.57234631e02, 1.40574757e02, 3.48347893e-02]),
            array([97.69973755, 57.21093674, 97.01760788]),
            array([260.11452637, 134.83022003, 1.46621812]),
            array([96.64759369, 57.30293846, 96.97781448]),
            array([262.0375885, 123.93178024, 1.88580176]),
            array([95.46563034, 58.44128761, 93.73796082]),
            array([261.11618347, 113.38555603, 13.15923586]),
            array([263.13592224, 108.65933075, 10.37897992]),
            array([263.31703796, 108.31037292, 7.83632045]),
            array([228.57422791, 198.64122009, -28.81009121]),
            array([123.77637253, 311.0098053, -26.76355705]),
            array([228.09718781, 199.453508, -26.04395466]),
            array([226.169133, 199.26845551, -24.63049984]),
            array([253.8026947, 72.11492691, 70.15319824]),
            array([258.40262756, 118.74311447, 6.46185772]),
            array([253.12166443, 67.99308929, 70.92814636]),
            array([259.04604797, 121.58326492, 5.67401767]),
            array([221.60127716, 205.89552765, -27.05329971]),
            array([260.43927307, 116.42729187, 5.77559032]),
            array([253.98069763, 65.07524338, 70.75127182]),
            array([260.37186279, 114.58317642, 8.26178377]),
            array([225.86286926, 204.75891266, -29.38810921]),
            array([245.7100174, 65.21211357, 73.8061058]),
            array([261.14040833, 112.50418625, 9.57530184]),
            array([261.58153381, 110.10290146, 7.77217808]),
            array([125.88637314, 296.42179871, -35.88405056]),
            array([245.27310791, 66.370047, 73.41165695]),
            array([214.83016052, 220.3297699, -37.1932272]),
            array([126.23728561, 299.13809814, -40.23581047]),
            array([247.88526459, 70.22501144, 72.57386017]),
            array([209.65634155, 227.39281006, -40.20807304]),
            array([246.44272003, 71.34965134, 73.17012634]),
            array([203.00903931, 219.68224182, -37.03164387]),
            array([205.00933838, 226.22361145, -38.22007637]),
            array([125.95667267, 212.62111053, 66.16587639]),
            array([122.73957901, 30.89734745, 94.9161377]),
            array([231.23873291, 205.8341156, -36.46622047]),
            array([127.36749954, 218.6457016, 65.68016281]),
            array([119.0247612, 35.86267929, 96.12893982]),
            array([228.06630554, 207.79863281, -36.5862154]),
            array([115.70569153, 39.44625206, 96.25898361]),
            array([228.62632294, 203.82817688, -35.8412075]),
            array([128.51858673, 219.00424957, 65.09199409]),
            array([120.28918762, 31.67502384, 95.75524521]),
            array([230.68367767, 201.21351166, -32.81178226]),
            array([125.85093155, 299.48922119, -26.88048191]),
            array([238.40518494, 91.43437729, 74.98796616]),
        ]
    )

    FRONT_SB_PSA = np.array(
        [
            array([231.56520996, 118.73776169, 70.91988602]),
            array([224.00072021, 168.74037476, -3.87976158]),
            array([218.78389893, 172.12254639, -0.76916977]),
            array([223.99143066, 168.70920563, -3.09412789]),
            array([240.00541992, 176.69556427, -11.27940831]),
            array([194.92542725, 170.04438629, 60.90227623]),
            array([233.13793793, 184.55710754, -6.11856747]),
            array([207.1467453, 180.43213654, 55.61075554]),
            array([249.73420868, 127.67181931, -6.91097342]),
            array([235.92649689, 178.06609192, -5.93888284]),
            array([235.93776093, 163.48214722, -9.94507179]),
            array([264.96479187, 122.21807404, 2.70690714]),
            array([230.154245, 157.39290924, -5.107056]),
            array([224.28890381, 162.73899384, -3.2167919]),
            array([189.74180756, 199.62716217, 58.19060745]),
            array([257.81962891, 124.15191956, 30.39377937]),
            array([221.94450989, 168.69324799, 1.01336183]),
            array([190.25965576, 201.18985291, 54.78376198]),
            array([191.4460022, 199.63731079, 52.77225266]),
            array([188.62742004, 208.64557953, 51.95754509]),
            array([258.33354034, 122.79793854, 23.84486675]),
            array([236.79761658, 104.41316299, 80.37585983]),
            array([188.28250885, 213.01910095, 50.28514366]),
            array([259.66039734, 118.08787994, 29.06682148]),
            array([238.32788696, 95.00508804, 80.60239563]),
            array([261.7823822, 112.88775635, 31.03274155]),
            array([234.54025116, 98.20358887, 81.26266632]),
            array([236.43467102, 93.70231018, 81.22091827]),
            array([204.47527771, 213.98109283, 5.33958179]),
            array([236.07241211, 96.55290909, 81.12759781]),
            array([204.31567993, 215.34455872, 3.92912261]),
            array([201.17944183, 211.68901672, 7.35520701]),
            array([201.56726837, 210.39047546, 13.89757586]),
            array([201.54600983, 211.46132965, 15.76373711]),
            array([187.67487946, 197.54305878, 76.98616714]),
            array([194.89660034, 215.99814148, 10.64578743]),
            array([252.25038452, 90.19731903, 74.99782486]),
            array([187.55140533, 202.76436768, 77.25716934]),
            array([250.25370789, 102.846418, 75.81716843]),
            array([196.60818329, 212.93979492, 7.86408088]),
            array([245.01072083, 93.15326843, 76.92873306]),
            array([188.85984344, 198.63237762, 75.59601974]),
            array([241.54283142, 84.72888336, 78.62677841]),
            array([243.51005707, 89.27089005, 78.29058685]),
            array([213.84859924, 242.00568695, -10.46259732]),
            array([211.33729706, 246.53116302, -7.33379777]),
            array([204.09425049, 254.80326691, -3.48404468]),
            array([191.42527161, 197.14768066, 79.35447693]),
            array([200.36689148, 256.52723999, 1.49684076]),
            array([252.82272949, 90.48093185, 73.66623459]),
            array([204.41569366, 251.27311859, 1.66821533]),
            array([188.67632294, 257.06810455, -0.92918699]),
            array([251.81956329, 93.36448975, 72.70717392]),
            array([200.95292206, 248.99784546, 4.34235316]),
            array([255.57770844, 83.20658264, 67.67793961]),
            array([205.29718323, 250.18286438, -3.12464315]),
            array([256.28606873, 84.56304169, 67.16375504]),
            array([208.56456604, 238.94094543, 0.83419601]),
            array([254.88481293, 80.37945251, 68.21702957]),
            array([266.82230835, 95.90316086, 64.12217789]),
            array([265.28704224, 98.50594788, 66.7965847]),
            array([101.52758026, 67.10254097, 93.67919846]),
            array([106.99581146, 73.54070587, 93.2215416]),
            array([99.60284576, 63.4193676, 94.58112717]),
            array([264.59560852, 103.89604797, 62.19345818]),
            array([97.22020111, 59.06165276, 95.04715881]),
            array([264.78725586, 100.48737717, 63.27321243]),
            array([192.00562592, 266.53103333, -10.56986039]),
            array([188.84827118, 271.70434265, -16.03259077]),
            array([259.82704468, 104.53373337, 66.36147919]),
            array([194.74097137, 262.62107544, -14.20987968]),
            array([188.08448334, 274.09262695, -14.9178381]),
            array([198.93763123, 257.96739197, -14.93494644]),
            array([190.76164246, 273.08349609, -17.44794846]),
            array([198.20938721, 259.52879333, -9.85213585]),
            array([195.90492554, 261.57504272, -4.64158432]),
            array([105.24988556, 56.22108955, 94.78215332]),
            array([188.61231995, 271.89032288, -8.23443985]),
            array([262.49989929, 103.96370239, 62.55763321]),
            array([106.00264664, 56.56028786, 94.71517029]),
            array([118.59939804, 41.39246254, 94.51817932]),
            array([121.94179993, 36.25911293, 94.692276]),
            array([263.15015869, 103.49919357, 64.51587029]),
            array([127.66149597, 33.13177147, 93.91045074]),
            array([261.88845825, 108.38950119, 65.32016144]),
            array([129.27416687, 26.19437523, 92.67916183]),
            array([116.33544235, 49.88900871, 94.92671509]),
            array([124.7083107, 33.54482918, 93.65885696]),
            array([99.70373077, 59.07975769, 94.61812286]),
            array([267.20201721, 96.8871933, 39.89472504]),
            array([100.55284653, 58.31376076, 95.83647156]),
            array([266.43119507, 99.55261536, 41.78441963]),
            array([268.02704773, 92.82565308, 39.03880463]),
            array([102.86439743, 58.78396568, 95.41866074]),
            array([101.60328598, 58.80700684, 95.63788223]),
            array([113.37508316, 50.07048264, 87.15476227]),
            array([111.11041946, 51.29042168, 89.79334106]),
            array([112.24985962, 51.53415718, 89.5869957]),
            array([259.98475952, 113.17684784, 23.95183411]),
            array([103.10081177, 58.04695969, 96.65682297]),
            array([267.81430054, 115.4555687, 22.37208996]),
            array([109.650737, 53.74387093, 96.40662842]),
            array([266.1921936, 119.3615181, 20.95835876]),
            array([108.71365433, 55.00773811, 96.35508652]),
            array([259.99251709, 119.2083107, 23.28139706]),
            array([104.21322479, 57.80518417, 96.86103973]),
            array([107.73868713, 56.01751404, 96.86685181]),
            array([112.19431534, 93.53319702, 84.16076622]),
            array([124.35674973, 118.48629951, 82.54654808]),
            array([112.82068863, 95.87341614, 83.39804535]),
            array([106.55668793, 82.12062531, 86.22858696]),
            array([268.89960632, 110.4302803, 8.82584825]),
            array([269.10704041, 113.72109909, 0.73190885]),
            array([181.27298279, 289.18789978, 41.42724113]),
            array([269.28114014, 112.55157242, -1.96223392]),
            array([184.30292816, 290.01023254, 38.92542992]),
            array([183.77279816, 286.38381653, 39.4298912]),
            array([268.1899353, 119.07017975, -0.43130476]),
            array([181.89295654, 286.64005127, 41.23975639]),
            array([181.3680954, 290.02225342, 40.79174767]),
            array([181.13087158, 284.3541748, 53.467939]),
            array([182.55261383, 280.21044312, 54.11246719]),
            array([182.86270752, 280.48217468, 53.90490685]),
            array([187.53273468, 279.21309204, 53.26477242]),
            array([273.23641968, 104.81648788, 9.29325647]),
            array([178.20558624, 297.71426697, -22.43024588]),
            array([272.31557617, 106.76859665, 12.75451517]),
            array([175.9603775, 297.96382446, -23.35005932]),
            array([183.55088196, 297.37707214, -39.36297569]),
            array([178.18892212, 302.4207489, -25.93928299]),
            array([182.3914566, 302.68016968, -33.27328949]),
            array([174.54564972, 290.75620422, 35.75253601]),
            array([183.24030914, 302.34555054, -35.96918449]),
            array([186.49380188, 295.72584534, -46.28443146]),
            array([179.40552826, 301.69456787, -27.63710804]),
            array([273.3225647, 115.70991974, -10.4067328]),
            array([274.06779785, 113.23302765, -8.0906714]),
            array([269.86724548, 110.40967789, -7.61107322]),
            array([269.66030273, 115.86371765, -4.50413126]),
            array([179.92188263, 290.35266418, 24.4434267]),
            array([184.35818634, 300.22356873, -42.46334648]),
            array([100.65591354, 59.10506516, 94.42329178]),
            array([176.55204163, 305.93936157, -26.35943394]),
            array([179.25759277, 304.42426147, -29.11073952]),
            array([179.75839081, 302.87324219, -43.95974884]),
            array([184.18895721, 296.9197876, 24.00174694]),
            array([101.24398041, 58.85817909, 94.31490936]),
            array([179.2057251, 303.16387329, -28.57243443]),
            array([183.65783844, 297.25605469, 23.81718426]),
            array([100.8193573, 59.04266357, 94.50344772]),
            array([180.33758698, 300.0675415, -33.0339016]),
            array([100.93463974, 58.95608139, 94.1574173]),
        ]
    )

    dataframe_vanilla = pd.DataFrame(FRONT, columns=["Velocity", "Height", "Energy"], index=FRONT[:, 0])
    dataframe_shared_buff_PSA = pd.DataFrame(FRONT_SB_PSA, columns=["Velocity", "Height", "Energy"], index=FRONT_SB_PSA[:, 0])
    sns.set_style("darkgrid")
    sns.color_palette("deep")
    sns.despine()

    plt.tight_layout()

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    x = dataframe_shared_buff_PSA["Velocity"]
    y = dataframe_shared_buff_PSA["Height"]
    z = dataframe_shared_buff_PSA["Energy"]

    ax.set_xlabel("Velocity")
    ax.set_ylabel("Height")
    ax.set_zlabel("Energy")

    ax.scatter(
        dataframe_vanilla["Velocity"],
        dataframe_vanilla["Height"],
        dataframe_vanilla["Energy"],
        label="MORL/D Vanilla",
        alpha=0.6,
    )
    ax.scatter(x, y, z, label="MORL/D-SB+PSA", alpha=0.6)
    plt.legend()
    sns.move_legend(
        ax,
        "lower center",
        bbox_to_anchor=(0.5, 1),
        ncol=2,
        title=None,
        frameon=False,
    )
    # plt.savefig("front_hopper.png", dpi=450)
    plt.show()
