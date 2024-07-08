from docx import Document
from docx.shared import Inches, Pt, Cm, Mm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.table import WD_ALIGN_VERTICAL
import io
from members.models import Clients
from num2words import num2words

def word_generate(clientArray):
    listOfClients = Clients.objects.get(id=clientArray[0])

    print(listOfClients.name)
    document = Document()
    # задаем стиль текста по умолчанию
    style = document.styles['Normal']
    style.font.name = 'Calibri'
    style.font.size = Pt(10)


    p = document.add_paragraph('Продавец: Мовсисян Э.Н.')
    paragraph_format = p.paragraph_format
    paragraph_format.line_spacing = 0.2

    p = document.add_paragraph('Адрес: 400096. ул. Удмуртская д.99 кв. 169')
    paragraph_format = p.paragraph_format
    paragraph_format.line_spacing = 0.2
    p = document.add_paragraph('ИНН: 344790398647')
    paragraph_format = p.paragraph_format
    paragraph_format.line_spacing = 0.2
    p = document.add_paragraph('Расчетный счет: 40802810514100011946')
    paragraph_format = p.paragraph_format
    paragraph_format.line_spacing = 0.2
    p = document.add_paragraph('Кор. счет: 30101810000000000201')
    paragraph_format = p.paragraph_format
    paragraph_format.line_spacing = 0.2
    p = document.add_paragraph('Банк: Фирма.Банк')
    paragraph_format = p.paragraph_format
    paragraph_format.line_spacing = 0.2
    p = document.add_paragraph('ИНН: 7702021163')
    paragraph_format = p.paragraph_format
    paragraph_format.line_spacing = 0.2
    p = document.add_paragraph('КПП: Фирма.КПП')
    paragraph_format = p.paragraph_format
    paragraph_format.line_spacing = 0.2
    p = document.add_paragraph('БИК: 044525201')
    paragraph_format = p.paragraph_format
    paragraph_format.line_spacing = 0.2
    p = document.add_paragraph('БИК: 044525201')
    paragraph_format = p.paragraph_format
    paragraph_format.line_spacing = 0.2
    p = document.add_paragraph('')

 
    # print(listOfClients[clientArray[0]])

    paragraph = document.add_paragraph('')
    paragraph_format = paragraph.paragraph_format
    paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = paragraph.add_run(listOfClients.name)
    # Форматируем текст прогона
    run.font.size = Pt(11)


    paragraph = document.add_paragraph('')
    paragraph_format = paragraph.paragraph_format
    paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = paragraph.add_run(f'Счет №1 от 22 января 2024г.на выполнение работ-услуг по договору №{listOfClients.documentNumber} от {listOfClients.documentDate}.')
    # Форматируем текст прогона
    run.font.size = Pt(11)
    run.font.bold = True

    newClArr = [[]]
    newClArr2 = ['', 'Итого:', '', '', '']
    i1 = 0
    for i , l in enumerate(clientArray[1]):

            newClArr[i].append(str(i+1))
            newClArr[i].append(l[0])
            newClArr[i].append('шт')
            newClArr[i].append(l[1])
            newClArr[i].append(l[2])
            newClArr[i].append(str(int(l[2]) * int(l[1])))
            i1 += int(l[2]) * int(l[1]);
    newClArr2.append(str(i1))
   
    col_names = [
        ['№', 'Наименование', 'Ед.изм.', 'Кол-во', 'Цена, руб.', 'Сумма, руб.'],
        *newClArr,
        newClArr2
    ]
    print(col_names)
    #（A）---------------------------------------------------------------------------------------------------------------
    # Obtain a 1-row, 3-column Table object
    # tb1 = doc1.add_table(rows=1, cols=len(col_names), style='Colorful Shading Accent 1')
    tb1 = document.add_table(rows=0, cols=0, style = 'Table Grid')
    tb1.add_column(Mm(12.0)) 
    tb1.add_column(Mm(52.0)) 
    tb1.add_column(Mm(17.0)) 
    tb1.add_column(Mm(18.0)) 
    tb1.add_column(Mm(25.0)) 
    tb1.add_column(Mm(29.0)) 


    for d in col_names:
        row = tb1.add_row()   # Add Row Object
        row.height = Mm(8.0)  # Specify row height as 8mm
        
        for i, cell in enumerate(row.cells): # Obtaining Cell object
            cell.text = d[i]                  # Set value to Cell object
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER # Set placement position in the cell




    p = document.add_paragraph(f'Сумма прописью: {num2words(i1, lang='ru')}  00коп. Без НДС.')
    paragraph_format = p.paragraph_format
    paragraph_format.line_spacing = 1.5
    p = document.add_paragraph('')

    p = document.add_paragraph('')

    paragraph = document.add_paragraph('')
    paragraph_format = paragraph.paragraph_format
    # paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = paragraph.add_run('Руководитель предприятия 	Фирма.Руководитель.ФИО	Бухгалтер 	Фирма.Бухгалтер.ФИО')
    # Форматируем текст прогона
    run.font.size = Pt(8)


    document.add_page_break()

    # document.save('demo.docx')
    # https://stackoverflow.com/questions/46011280/how-to-generate-a-docx-in-python-and-save-it-in-memory
    file_stream = io.BytesIO()
    # Save the .docx to the buffer
    document.save(file_stream)
    # Reset the buffer's file-pointer to the beginning of the file
    file_stream.seek(0)

    return file_stream