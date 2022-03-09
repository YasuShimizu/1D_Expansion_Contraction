import main

#'Q10-1' #Q=10 急拡　実験と同じ初期河床
#'Q10-2' #Q=10 急拡　平坦初期河床
#'Q10-3' #Q=10 急拡　初期河床を上記より若干緩く
#'Q15-1' #Q=15 急縮　実験と同じ初期河床
#'Q15-2' #Q=15 急縮　平坦初期河床
#'Q15-3' #Q=15 急縮　初期河床を上記より若干急に

runs=["Q10-1","Q10-2","Q10-3","Q15-1","Q15-2","Q15-3"]

for case_name in runs:
    print(case_name)
    main.nays1d_Mini(case_name)
