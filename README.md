Pipeline Functionality

The Pipleine program serves as a central collating hub for the small sub-routines found in the src file. The file functions by accepting commandline declarations of input files, output destinations, and a config file location, in addition to a verbosity declaration which ennumarates the various logger statuses throughout the program. The config file, found in this program package is located in the config/ directory, and provides infomation on required columns, filtering methods, and which columns should contain numeric values. The input is argument is validated, along with the config file, to ensure that they exist and are valid files initially. It then loads the input file into a dataframe, and the config file into a dictionary which it stores to be refered to later. Then it runs the validate_dataframe function, which both ensures that all required columns are present (as dictated by the config file) and that there are no missing elements or non-numeral elements in numeric-designated columns. It then processes the data and removes outliers as dictated by the config file, before returning a report of the changes made by processing and saving the new csv to the designated output location and directory.

DECLARATION

I had a number of issues throughout the process of assembling this process, these issues where recurring and I was not able to consitently able to find solutions to them through either help from the TAs in class or through independant researching on forumns or consulting AI chatbots (somthing that was suggested by one of the TAs to do) or closing and opening various programs and virtual environments. As a result, I am not able to fully confirm the working capacity of the final product. However, I am reasonably confident in my understading of the project, what each subroutine required and how they performed, and the nature of the coding language and process as a whole. As a result, I am hopefully optimistic that running the program on a different, properly opperating environment would lead to sucessful returns, or at least close to full functionality.

Example command
Using my understanding of the code structure, the following command should return the following result, or something very simmilar.

-> python3 pipeline.py --input fixtures/sample_data.csv --config config/config.yaml --output output/processed_csv.csv

|
-> File would return a csv excluding the rows 94,95, and 96 (ID 95-97) as they do not contain valid numericals in the     
    ratings column,rows indexed 98 and 99 removed for being duplicates of the first two rows (0 and 1)
    as well as excluding rows 92 and 93 (ID 93 and 94), as their scores of -50 and 200 fall outside of the accepted range of 3 standard deviations (calcuated at a single St.Dv. of ~20.22, and so a "normal" range of ~15 to 135, assuming normal distribution, which there is no clear indicator to suggest the data may not be normally distributed given no clear rating system is established.) It would also include a dictionary report of 100 initial rows, 5 were removed, leaving 93 rows remaining and all columns remaining