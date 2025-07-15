import numpy as np

# 파일 경로 설정
qe_output_file = "/Users/seyeong/Desktop/UNIST/25winter/HandsOn/lab6/Au/au_50.out"

# Extended XYZ 파일 경로 설정
xyz_file = "/Users/seyeong/Desktop/UNIST/25winter/HandsOn/lab6/Au/au_structure.xyz"

# Extended XYZ 파일 내용
xyz_content = """12
Lattice="7.882593 0.000000 0.000000 0.000000 7.882593 0.000000 0.000000 0.000000 7.882593" Properties=species:S:1:pos:R:3
Au 0.000000 0.000000 0.000000
Au 3.941297 3.941297 0.000000
Au 3.941297 0.000000 3.941297
Au 0.000000 3.941297 3.941297
"""

# Extended XYZ 파일 쓰기
with open(xyz_file, 'w') as file:
    file.write(xyz_content)

print("Extended XYZ file has been generated.")