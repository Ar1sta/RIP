from operator import itemgetter
 
class PC:
    """Компьютер"""
    def __init__(self, id, name, os):
        self.id = id
        self.pcname = name
        self.os = os
        
class Program:
    """Программа"""
    def __init__(self, id,name,memory, pc_id):
        self.id = id
        self.programname = name
        self.memory=memory
        self.pc_id = pc_id
 
class ProgramPC:
    """
    'Программы компьютера' для реализации 
    связи многие-ко-многим
    """
    def __init__(self, pc_id, program_id):
        self.pc_id = pc_id
        self.program_id = program_id
 
# Программы
programs = [
    Program(1, 'Visual Studio',30,1),
    Program(2, 'Visual Studio',30,2),
    Program(3, 'Visual Studio',30,3),
    Program(4, 'Visual Studio',30,5),
    Program(5, 'Qlick Sense',3,2),
    Program(6, 'SQL Server Managment Studio',1,1),
    Program(7, 'SQL Server Managment Studio',1,5),
    Program(8, 'Microsoft Office 2016',9,1),
    Program(9, 'Adobe Acrobat Reader',0.1,4),
    Program(10, 'Adobe Acrobat Reader',0.1,5),
    Program(11, 'Safari',0.2,3),
    Program(12, 'MATLAB',6,2),
    Program(13, 'OpenOffice',0.2,4),
    Program(14, 'Visual Studio',30,4),
]
 
# Сотрудники
pcs = [
    PC(1, 'Asus', 'Windows'),
    PC(2, 'Acer', 'Windows'),
    PC(3, 'Apple','MacOS'),
    PC(4, 'Dell', 'Linux'),
    PC(5, 'Lenovo', 'Windows'),
]
 
pcs_programs = [
    ProgramPC(1,1),
    ProgramPC(1,6),
    ProgramPC(1,8),
    ProgramPC(2,2),
    ProgramPC(2,5),
    ProgramPC(2,12),
    ProgramPC(3,3),
    ProgramPC(3,11),
    ProgramPC(4,9),
    ProgramPC(4,13),
    ProgramPC(5,4),
    ProgramPC(5,7),
    ProgramPC(5,10),    
]
def main():
    """Основная функция"""

    one_to_many = [(d.programname, d.memory, e.pcname, e.os) 
        for d in programs 
        for e in pcs
        if d.pc_id==e.id]
    
    print('Задание А1')
    res_1 = sorted(one_to_many, key=itemgetter(2))
    print(res_1)
    
    print("\nЗадание А2:")    
    res2 = []     
    for p in pcs:       
        a = sum([k.memory for k in programs if (k.pc_id == p.id)])   
        res2.append([p.pcname, a])   
    res2=sorted(res2,key=itemgetter(1))
    print(res2) 

    print("\nЗадание А3:")     
    many_to_many_temp = [(l.pcname, l.os, m.program_id)         
        for l in pcs         
        for m in pcs_programs         
        if (l.id == m.pc_id)     
    ]     
    many_to_many = [(j.programname, j.memory, pcname, os)         
        for pcname, os, program_id in many_to_many_temp         
        for j in programs         
        if (j.id == program_id)     
    ]     
    res3 = {}     
    for l in pcs:         
        if 'A' in l.pcname:             
            Pcs = list(filter(lambda x: x[2] == l.pcname ,many_to_many))             
            Programms = [programname for programname, mem, pcname, os in Pcs]            
            res3[l.pcname] = Programms    
    print(res3) 
if __name__ == '__main__':
    main()
