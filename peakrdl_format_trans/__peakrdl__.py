from format_translator import format_translator
from rkvGensystemRDL import GensystemRDL
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import argparse
class MyExporterDescriptor:
    short_desc = ".transfer csv/xlxs  to rdl."
    long_desc = "..."

    def add_exporter_arguments(self, arg_group: 'argparse.ArgumentParser') -> None:
        arg_group.add_argument("-xlsx", help="display a path of csv file", type=str)
        arg_group.add_argument("-csv", help="display a path of csv file", type=str)

    def do_export(self,  options: 'argparse.Namespace') -> None:
        
        format_trans=format_translator()
        if not os.path.exists(options.xlsx):
            print('%s \nEXCSL FILE PATH NOT EXISTS \n%s\n' % (40*'*', 40*'*'))
            print('ERROR')
            exit()
        print(options.xlsx)
      # if((args.csv==False)&&(args.xlsx)):
      #     print('%s \nXLSX TRANSFER TO RDL started \n%s\n' % (40 * '*', 40 * '*'))
      # if (args.csv == True && args.xlsx==False):
      #     print('%s \nCSV TRANSFER TO RDL started \n%s\n' % (40 * '*', 40 * '*'))
      # if (args.csv == False && args.xlsx==False):
      #     print('%s \n NO PARAMETER ARGS INPUT \n%s\n' % (40 * '*', 40 * '*'))
        if not os.path.exists(options.xlsx):
            print('%s \nEXCSL FILE PATH NOT EXISTS \n%s\n' % (40*'*', 40*'*'))
            print('ERROR')
            exit()
        print(options.xlsx)
        if(options.xlsx):
            format_trans.XLSX2CSV(options.xlsx)
        print('%s \n transfer success \n%s' % (40*'*', 40*'*'))
        gen = GensystemRDL()
        gen.readRgmFile(format_trans.csv_name)
        gen.gensystemRDLFile()
        print('%s \ntransfer success \n%s' % (40*'*', 40*'*'))