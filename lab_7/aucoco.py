import numpy as np
import matplotlib.pyplot as plt

# 파일 경로 설정 (C와 O의 s, p 오비탈 PDOS 파일)
# 흡착 전
c_s_file_before = "/Users/seyeong/Desktop/UNIST/25winter/HandsOn/lab7/co.pdos.dat.pdos_atm#1(C)_wfc#1(s)"
c_p_file_before = "/Users/seyeong/Desktop/UNIST/25winter/HandsOn/lab7/co.pdos.dat.pdos_atm#1(C)_wfc#2(p)"
o_s_file_before = "/Users/seyeong/Desktop/UNIST/25winter/HandsOn/lab7/co.pdos.dat.pdos_atm#2(O)_wfc#1(s)"
o_p_file_before = "/Users/seyeong/Desktop/UNIST/25winter/HandsOn/lab7/co.pdos.dat.pdos_atm#2(O)_wfc#2(p)"

# 흡착 후
c_s_file_after = "/Users/seyeong/Desktop/UNIST/25winter/HandsOn/lab7/auab.pdos.dat.pdos_atm#13(C)_wfc#1(s)"
c_p_file_after = "/Users/seyeong/Desktop/UNIST/25winter/HandsOn/lab7/auab.pdos.dat.pdos_atm#13(C)_wfc#2(p)"
o_s_file_after = "/Users/seyeong/Desktop/UNIST/25winter/HandsOn/lab7/auab.pdos.dat.pdos_atm#14(O)_wfc#1(s)"
o_p_file_after = "/Users/seyeong/Desktop/UNIST/25winter/HandsOn/lab7/auab.pdos.dat.pdos_atm#14(O)_wfc#2(p)"

# 데이터 로드 함수
def load_pdos(file, columns):
    data = np.loadtxt(file)
    energy = data[:, 0]  # 첫 번째 열: 에너지 (eV)
    pdos = np.sum(data[:, 1:columns+1], axis=1)  # 두 번째 열 이후: PDOS 값 합계
    return energy, pdos

# 데이터 로드 (흡착 전)
energy_c_s_before, pdos_c_s_before = load_pdos(c_s_file_before, 1)
energy_c_p_before, pdos_c_p_before = load_pdos(c_p_file_before, 3)
energy_o_s_before, pdos_o_s_before = load_pdos(o_s_file_before, 1)
energy_o_p_before, pdos_o_p_before = load_pdos(o_p_file_before, 3)

# 데이터 로드 (흡착 후)
energy_c_s_after, pdos_c_s_after = load_pdos(c_s_file_after, 1)
energy_c_p_after, pdos_c_p_after = load_pdos(c_p_file_after, 3)
energy_o_s_after, pdos_o_s_after = load_pdos(o_s_file_after, 1)
energy_o_p_after, pdos_o_p_after = load_pdos(o_p_file_after, 3)

# 그래프 그리기
plt.figure(figsize=(12, 8))

# 흡착 전
plt.plot(energy_c_s_before, pdos_c_s_before, label="C s-orbital (before)", linestyle="--", color="blue")
plt.plot(energy_c_p_before, pdos_c_p_before, label="C p-orbital (before)", linestyle="-", color="blue")
plt.plot(energy_o_s_before, pdos_o_s_before, label="O s-orbital (before)", linestyle="--", color="red")
plt.plot(energy_o_p_before, pdos_o_p_before, label="O p-orbital (before)", linestyle="-", color="red")

# 흡착 후
plt.plot(energy_c_s_after, pdos_c_s_after, label="C s-orbital (after)", linestyle="--", color="green")
plt.plot(energy_c_p_after, pdos_c_p_after, label="C p-orbital (after)", linestyle="-", color="green")
plt.plot(energy_o_s_after, pdos_o_s_after, label="O s-orbital (after)", linestyle="--", color="orange")
plt.plot(energy_o_p_after, pdos_o_p_after, label="O p-orbital (after)", linestyle="-", color="orange")

# Fermi Energy 기준선 (보통 E_F = 0 eV로 설정)
plt.axvline(x=0.0, color="black", linestyle="--", label="Fermi Level")

# 그래프 설정
plt.xlabel("Energy (eV)")
plt.ylabel("Projected DOS")
plt.title("Projected Density of States (C, O) Before and After Adsorption")
plt.legend()
plt.grid()

# 그래프 표시
plt.show()