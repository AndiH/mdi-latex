tail -n +20 ../MaterialDesign-Webfont/css/materialdesignicons.css | head -n -255 | grep -A 3 "mdi-" | sed 's#.mdi-##' | sed 's#::before {##' | sed 's#content: "\\##' | sed 's#";##' | sed 's#}##' | tr -s '\n' | sed 'N;s#\n  #,#' > materialdesignicons.csv
