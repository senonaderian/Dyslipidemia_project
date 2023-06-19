import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('result.csv')

# Drop the columns named 'column1' and 'column2'
df = df.drop(columns=['codkhanevar', 'codkhooshe', 'namshahr', 'mosahebekonnande', 'nam',
                      'tedadkoodakzire6', 'tel', 'mob', 'address', 'age10sal', 'diabet',
                      'ezterab', 'fesharekhoon', 'hamlegalbi', 'sektemagzi', 'saratan',
                      'asm', 'kamkhooni', 'charbiekhoon', 'kabedcharb', 'vitD', 'shoglsarparas',
                      'vazn', 'gad', 'BMI', 'dorkamar', 'dorekamarbala', 'dorbasan', 'dorkamarbebasan',
                      'WbeHmardan', 'WbeHzanann', 'fesharsis', 'feshardias', 'sisrotbe', 'diasrotb',
                      'senegaedegi', 'seneiaesegi', 'bardariashirde', 'senekoodak', 'vazkoodak',
                      'gadkoodak', 'daroofeshar', 'daroogand', 'daroocharbi', 'masrafedaroo',
                      'sigar1', 'Q1b', 'sigar2', 'Q2b', 'sigar3', 'Q3a', 'Q3b', 'sigar4', 'Q4a',
                      'Q4b', 'sigar5', 'sigar6', 'sigar7', 'sigar8', 'sigar9', 'sigar10',
                      'sigar11', 'sigar12', 'sigar13', 'sigar14', 'sigar15', 'sigar16',
                      'sigar17', 'sigar18', 'sigar19', 'sigar20', 'sigar21', 'sigar22',
                      'sigar23', 'sigar24', 'sigar25', 'sigar261', 'Q262', 'Q263', 'Q264',
                      'Q265', 'sigar27', 'sigar28', 'sigar29', 'sigar301', 'Q302', 'Q303',
                      'Q304', 'Q305', 'roz1', 'roz2', 'ros2tagir', 'roz3', 'roz4', 'roz5',
                      'ros5tagir','roz6', 'roz7', 'roz8', 'WHS2', 'WHS3', 'WHS4',
                      'WHS5', 'WHS6', 'WHS7', 'WHS8', 'WHS9', 'WHS10', 'faliat11', 'faliat12',
                      'faliat21', 'faliat22', 'faliat31', 'faliat32', 'faliat41', 'faliat42',
                      'faliat51', 'faliat52', 'faliat61', 'faliat62', 'faliat63', 'faliat71',
                      'faliat72', 'faliat73', 'GAD1', 'GAD2', 'GAD3', 'GAD4', 'GAD5', 'GAD6',
                      'GAD7', 'GADkoll', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q110',
                      'Q120', 'Imeni1', 'Imeni2', 'Imeni3', 'Imeni4', 'Imeni5', 'Imeni61', 'Imeni62',
                      'Imeni63', 'Imeni64', 'Imeni65', 'Imeni7', 'Imeni8', 'Imeni9', 'Imeni10', 'Imeni11',
                      'Imeni12', 'Imeni131', 'Imeni132', 'Imeni133', 'Imeni134', 'Imeni135', 'Imeni14',
                      'Imeni15', 'Imeni16', 'Imeni17', 'Imeni18', 'Imeni19', 'Imeni20', 'Imeni21', 'Imeni22',
                      'Imeni23', 'Imeni24', 'Imeni25', 'Imeni26', 'Imeni27', 'Imeni28', 'Imeni29', 'Imeni30',
                      'Imeni31', 'Imeni32', 'naamni1', 'naamni2', 'naamni3', 'naamni4', 'naamni5', 'naamni6',
                      'Q11', 'Q12', 'Q21', 'Q22', 'Q31', 'Q32', 'Q41', 'Q42', 'Q51', 'Q52', 'Q61', 'Q62',
                      'Q71', 'Q72', 'diabetcas', 'filter_$', 'sodiuedra', 'potasiuedr', 'creatinedr', 'creatinimmol',
                      'prcr24', 'sodium24edr', 'nacldariaftipredictiv', 'saranenamak', 'saranesangnamak',
                      'saranesang4', 'saranenamakk', 'saranemasrafenamak', 'intersalt', 'intersaltgr',
                      'gandsara', 'shekarsara', 'shekarvagandsara', 'saranrogmaie', 'saranrogjamed', 'saranrogan',
                      'vitDserkam', 'saranenamakbala', 'naclpredbala', 'ezafevazn', 'chgh', 'shahrroosta',
                      'proffetion', 'ezafechagh', 'conicityindex', 'waisttoheight', 'NTI001', 'shahrepurmia', 'NFAC3_1',
                      'NFAC1_1', 'NFAC2_1', 'FAC1_1', 'FAC2_1', 'FAC3_1'])


# Save the modified DataFrame to a new CSV file
df.to_csv('output1.csv', index=False)
