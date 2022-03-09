import main

#'Q10-1' #Q=10 急拡　実験と同じ初期河床
#'Q10-2' #Q=10 急拡　平坦初期河床
#'Q15-1' #Q=15 急縮　実験と同じ初期河床
#Q15-2' #Q=15 急縮　平坦初期河床

#runs=["Q10-1","Q10-2","Q10-3","Q15-1","Q15-2","Q15-3"]
runs=["Q15-1","Q15-2"]

for case_name in runs:
    print(case_name)
    main.nays1d_Mini(case_name)
