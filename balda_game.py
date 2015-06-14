from tkinter import *
import tkinter
import random

def begin_game(root):
	for j in range(5):
		letters[10 + j] = first_word[0][j]
	redraw(field)
	but.destroy()
	lab.destroy()
	lab_1 = Label(fra1, text=" Введите букву в строку, затем нажатием правой клавишей мыши выберите клетку для неё. \n  Выделите своё слово(нажатие левой клавишей мыши - начало и конец выделения) ", font="Arial 12")
	lab_1.pack()
	lab_2 = Label(root_2, text = first_word[0] , font="Arial 18")
	lab_2.grid(padx = 50)
	lab_2.pack()
	ent.delete(0, END)
	dictionary[first_word[0]] = 10
	words.append(first_word[0])
	mode[0] = 'none' 
def redraw(canvas):
	for i in range(0, side, size):
		for k in range(0, side, size):
			canvas.create_rectangle(i, k, i+size, k+size, outline = 'blue', fill = 'white')
	making_mark(current_letter[2], current_letter[3], 'green')
	for x in range(len(letters)):
		canvas.create_text(x%cells * size + size//2, x //cells * size + size//2, text = letters[x])

def error_messege_add_to_dictionary(root, text, func):
		win = Toplevel(root, relief=SUNKEN, bd=10, bg="red")
		win.minsize(width=400, height=200)
		lab_3 = Label(win, text = 'Слова нет в словаре. Добавить его в словарь' + text , font="Arial 18", bg = 'red')
		lab_3.pack()
		but_2 = Button(win)
		but_2['text'] = 'Да'
		but_2['bg'] = 'blue'
		but_2['fg'] = 'yellow'
		but_2.bind('<Button-1>', func)
		but_2.pack()
		but_1 = Button(win)
		but_1['text'] = 'Нет'
		but_1['bg'] = 'blue'
		but_1['fg'] = 'yellow'
		but_1.bind('<Button-1>', OK_new_letter)
		but_1.pack()
		windows[0] = win
def error_messege(root, text):
	if windows[0] != 0:
		windows[0].destroy()
	win = Toplevel(root, relief=SUNKEN, bd=10, bg="red")
	win.minsize(width=400, height=200)
	lab_3 = Label(win, text = text , font="Arial 18", bg = 'red')
	lab_3.pack()
	but_1 = Button(win)
	but_1['text'] = 'OK'
	but_1['bg'] = 'blue'
	but_1['fg'] = 'yellow'
	but_1.bind('<Button-1>', OK)
	but_1.pack()
	windows[0] = win
def OK(event):
	global current_word_numbers
	windows[0].destroy()
	current_word_numbers = []
def add_first_word_event(event):
	windows[0].destroy()
	begin_game(root)
def add_word_event(event):
	windows[0].destroy()
	add_word(current_word)
def add_word(current_word):
	global current_word_numbers
#	print(current_word_numbers)
#	print(current_word)
	dictionary[current_word[0]] = 10
	words.append(current_word[0])
	points[mode[3]] += len(current_word[0])
	info = current_word[0] + '(' + str(len(current_word[0])) + ', ' + str(points[mode[3]]) + ')'
	current_word_numbers = []
#	print(points)
#	print(words)
	counter[0] += 1
	if mode[2] == 'computer':
		words_and_points.create_text(75, counter[0]*10, text = info, font = 'Arial 12')	
		computer(current_word)
	else:
		current_letter[0] = ''
		current_letter[2] = 100500
		mode[1] = True
		current_word[0] = ''
		if mode[3] == 0:
			mode[3] = 1
			words_and_points.create_text(75, counter[0]*10, text = info, font = 'Arial 12')
			error_messege(root, 'Ход второго игрока')
		else:
			words_and_points.create_text(75 + 150, (counter[0] - 1) *10, text = info, font = 'Arial 12')
			mode[3] = 0
			if counter[0] != 20:
				error_messege(root, 'Ход первого игрока')
			else:
				victory(mode)
def starter(event):
	boole = True
	first_word[0] = ent.get()
	if len(first_word[0]) == 5:
		for x in first_word[0]:
			if x.isupper():
				error_messege(root, 'Используйте только маленькие буквы')
				boole = False
		if first_word[0] in dictionary:
			begin_game(root)
		else:
			if boole:
				error_messege_add_to_dictionary(root, ' и начать игру?', add_first_word_event)
	else:
		error_messege(root, 'В слове должно быть ПЯТЬ букв')
def OK_new_letter(event):
	global current_word_numbers
	current_word[0] = ''
	windows[0].destroy()
	current_word_numbers = []
	current_letter[0] = ''
	current_letter[2] = 100500
	letters[current_letter[1]] = ' '
	mode[1] = True	
	redraw(field)
def mark(event):
	global current_word_numbers
	field = event.widget
	x = event.x
	y = event.y
	x = x // size * size
	y = y // size * size
	number = x // size + y // size * cells
	if mode[0] == 'mark':
		if letters[number] != ' ':
			if abs(number - current_word_numbers[len(current_word_numbers)-1]) != 4 and abs(number - current_word_numbers[len(current_word_numbers)-1]) != 6:
#				making_mark(x, y, 'red')
				if number in current_word_numbers:
					if number == current_word_numbers[len(current_word_numbers)-1]:
						pass
					else:
						error_messege(root, 'Нельзя выделять одну и ту же клетку дважды')
						current_word_numbers = []
						mode[0] = 'none'
						redraw(field)
				else:
					making_mark(x, y, 'red')					
					current_word_numbers.append(number)
			else:
				error_messege(root, 'Нельзя выделять клетки по диагонали(через узел клетки)')
				urrent_word_numbers = []
				mode[0] = 'none'
				redraw(field)			
		else:
			error_messege(root, 'Можно выделять только клетки с буквами')
			current_word_numbers = []
			mode[0] = 'none'
			redraw(field)

def start_or_end_marking(event):
	global current_word_numbers
	if mode[0] != 'not begin yet':
		x = event.x
		y = event.y
		x = x // size * size
		y = y // size * size
		number = x // size + y // size * cells
		if mode[0] == 'mark':	
			mode[0] = 'none'
			if current_letter[1] in current_word_numbers:
				for x in current_word_numbers:
					current_word[0] += letters[x]
				if current_word[0] in words:
					error_messege(root, 'Это слово уже использовалось')
					current_word[0] = ''
					current_word_numbers = []
					current_letter[0] = ''
					current_letter[2] = 100500
					letters[current_letter[1]] = ' '
					mode[1] = True	
					redraw(field)
				else:
					if current_word[0] in dictionary:
						add_word(current_word)
					else:
						error_messege_add_to_dictionary(root, ' и продолжить игру?', add_word_event)
					redraw(field)
			else:
				error_messege(root, 'Слово должно содержать букву, которую вы поставили в этот ход')
				current_word_numbers = []
				redraw(field)
		else:
			if current_letter[0] != '':
				if letters[number] != ' ':
					making_mark(x, y, 'red')
					current_word_numbers.append(number)
					mode[0] = 'mark'
				else:
					error_messege(root, 'Нужно начать выделение с клетки с буквой')
			else:
				error_messege(root, 'Поставьте букву (введите её в строку, а затем выберите клетку правой клавишей мыши')	
	else:
		error_messege(root, 'Введите слово из пяти букв')
def making_mark(x, y, colour):
	x_1 = x + size
	y_1 = y + size
	field.create_line(x, y, x_1, y, fill = colour)
	field.create_line(x, y, x, y_1, fill = colour)
	field.create_line(x_1, y, x_1, y_1, fill = colour)
	field.create_line(x, y_1, x_1, y_1, fill = colour)


def surroundings(number):
	surroundings_bool = True
	surroundings = []
	if 0 < number < 4:
		surroundings.append(number + 1)
		surroundings.append(number - 1)
		surroundings.append(number + cells)
		if letters[number + 1] == ' ' and letters[number - 1] == ' ' and letters[number + cells] == ' ':
			surroundings_bool = False
	if 20 < number < 24:
		surroundings.append(number + 1)
		surroundings.append(number - 1)
		surroundings.append(number - cells)
		if letters[number + 1] == ' ' and letters[number - 1] == ' ' and letters[number - cells] == ' ':
			surroundings_bool = False
	if 0 == number:
		surroundings.append(number + 1)
		surroundings.append(number + cells)
		if letters[number + 1] == ' ' and letters[number + cells] == ' ':
			surroundings_bool = False
	if 4 == number:
		surroundings.append(number - 1)
		surroundings.append(number + cells)
		if letters[number - 1] == ' ' and letters[number + cells] == ' ':
			surroundings_bool = False
	if 20 == number:
		surroundings.append(number + 1)
		surroundings.append(number - cells)
		if letters[number + 1] == ' ' and letters[number - cells] == ' ':
			surroundings_bool = False
	if 24 == number:
		surroundings.append(number - 1)
		surroundings.append(number - cells)
		if letters[number - 1] == ' ' and letters[number - cells] == ' ':
			surroundings_bool = False
	if 4 < number < 20:
		if number // cells == 0:
			surroundings.append(number + 1)
			surroundings.append(number - cells)
			surroundings.append(number + cells)
		else:
			if number % cells == 4:
				surroundings.append(number - 1)
				surroundings.append(number - cells)
				surroundings.append(number + cells)
			else:
				surroundings.append(number + 1)
				surroundings.append(number - cells)
				surroundings.append(number + cells)
				surroundings.append(number - 1)			
	return [surroundings_bool, surroundings]

def put_letter(event):
	global current_word_numbers
	if mode[0] != 'not begin yet': 
		if mode[1]:
			x = event.x
			y = event.y
			x = x // size * size
			y = y // size * size
			number = x // size + y // size * cells
			l = ent.get()
			if l.isalpha():
				if len(l) == 1:
					if l.islower():
						if letters[number] == ' ':						
							if surroundings(number)[0]:
								current_letter[0] = l		
								letters[number] = current_letter[0]
								current_letter[1] = number
								current_letter[2] = x
								current_letter[3] = y
								redraw(field)
								ent.delete(0, END)
								mode[1] = False
							else:
								error_messege(root, 'Клетка, в которую можно поставить букву, \n должна иметь общую сторону хотя бы с одной клеткой, уже содержащей букву')
						else:
							error_messege(root, 'Поставьте букву в свободную клетку')
					else:
						error_messege(root, 'Используйте только маленькие буквы')
				else:
					error_messege(root, 'Нужно ввести ОДНУ букву')
					ent.delete(0, END)
			else:
				if l == '':
					error_messege(root, 'Нужно СНАЧАЛА ввести букву, а потом щелчком правой клавишей мыши выбрать для неё место')
					ent.delete(0, END)
				else:
					error_messege(root, 'Нужно ввести БУКВУ')
					ent.delete(0, END)
		else:
			error_messege(root, 'Вы уже поставили букву, выделите слово')
			redraw(field)
			current_word_numbers = []
	else:
		error_messege(root, 'Введите слово из пяти букв')
def computer(current_word):
	global current_word_numbers
	global computers_word
	counter[0] += 1
	leng = len(current_word[0])
	current_word_numbers = []
	current_word[0] = ''
	if counter[0] % x_number[0] != 0:
		length = (random.randrange(100) % 3 - 1) + leng
	else:
		if points[0] - points[1] > 3:
			length = points[0] - points[1]
		else:
			length = 3
	if length > 9:
		length = 9
	if length < 3:
		length = 3
	search(length)
def end(a):
	global computers_word
	print(computers_word)
	current_letter[0] = ''
	current_letter[2] = 100500
	mode[1] = True
	redraw(field)
	points[1] += len(computers_word[0])
	words.append(computers_word[0])
	info = computers_word[0] + '(' + str(len(computers_word[0])) + ', ' + str(points[1]) + ')'
	words_and_points.create_text(75 + 150, (counter[0] - 1) *10, text = info, font = 'Arial 12')
	letters[computers_word[1]] = computers_word[2]
	redraw(field)
	computers_word = ['first', -1, '']
	if counter[0] < 20:
		error_messege(root, 'Ваш ход')
	else:
		victory(mode)
def search(length):
	for number in range(len(letters)):
		x = letters[number]
		if letters[number] == ' ':
			if surroundings(number)[0]:
				computers_word_number[0] = number
				for l in alphabet:
					computers_word_letter[0] = l
					letters[number] = l
					for k in range(len(letters)):
						if letters[k] != ' ':
							if surroundings(k)[0]:
								w = [letters[k], [k]]
								add_letter_to_word_computer(k, w, length)
					letters[number] = ' '
	if computers_word[0] == 'first':
		length -= 1
		print(computers_word)
		search(length)
	else:
		end(1)
def add_letter_to_word_computer(number, word, length):
	for x in surroundings(number)[1]:
		if letters[x] != ' ':
			if x in word[1]:
				pass 
			else:
				new = [word[0] + letters[x], word[1]]
				new[1].append(x)
				print(new)
				if len(new[0]) < length:
					add_letter_to_word_computer(x, new, length)
				else:
					if new[0] in dictionary:
						if new[0] in words:
							pass
						else:
							if computers_word_number[0] in new[1]:
								if dictionary[new[0]] > dictionary[computers_word[0]]:
									print(new)
									computers_word[0] = new[0]
									computers_word[1] = computers_word_number[0]
									computers_word[2] = computers_word_letter[0]
									print(computers_word_number)



def game_with_man(event):
	mode[2] = 'man'	
	windows[0].destroy()
	field.pack()
	fra1.pack()
	fra2.pack()
	ent.pack()
	but.pack()
	lab.pack()

def game_with_computer(event):
	mode[2] = 'computer'
	windows[0].destroy()
	field.pack()
	fra1.pack()
	fra2.pack()
	ent.pack()
	but.pack()
	lab.pack()

def victory(mode):
	if mode[2] == 'computer':
		if points[0] == points[1]:
			error_messege(root, 'Игра окончена \n Ничья')
		else:
			if points[0] < points[1]:
				error_messege(root, 'Игра окончена \n Вы проиграли')
			else:
				error_messege(root, 'Игра окончена \n Вы победили')	
	else:
		if points[0] == points[1]:
			error_messege(root, 'Игра окончена \n Ничья')
		else:
			if points[0] > points[1]:
				error_messege(root, 'Игра окончена \n Победил первый игрок')
			else:
				error_messege(root, 'Игра окончена \n Победил второй игрок')


alphabet = ['й', 'ц', 'у', 'к', 'е', 'н', 'г', 'ш', 'щ', 'з', 'х', 'ъ', 'ф', 'ы', 'в', 'а', 'п', 'р', 'о', 'л', 'д', 'ж', 'э', 'я', 'ч', 'с', 'м', 'и', 'т', 'ь', 'б', 'ю', 'ё']
side=250 
size = 50 
cells = side // size
letters = [ ' ' for x in range (25)]
mode = ['not begin yet', True, 'computer', 0]
first_word = ['']
current_letter = ['', -1, -100500, -100500]
current_word_numbers = []
current_word = ['']
computers_word = ['first', -1, '']
computers_word_number = [-1]
computers_word_letter = ['']
dictionary = {}
words =[]
windows = [0]
points = [0 , 0]
counter = [0]
x = random.randrange(1000)
if x % 2 == 0:
	x = 4
else:
	x = 3
x_number = [x]



root = Tk()
root_2 = Tk()
ent = Entry(root, width=20, bd=5, fg = 'blue')
field = tkinter.Canvas(width=side, height=side, bg = 'white')
words_and_points = tkinter.Canvas(root_2, width = 300, height  = 400, bg = 'white')

fra1 = Frame(root, width=500, height=200, bg="white", bd = 20)
fra2 = Frame(root, width=300, height=200, bg="white", bd = 20)

but = Button(fra2)
but['text'] = 'Начать игру'
but['bg'] = 'blue'
but['fg'] = 'yellow'

lab = Label(fra1, text=" Введите первое слово (из пяти букв) ", font="Arial 18")







with open('out_file.txt') as current_file:
	for line in current_file:
		for word in line.rstrip().split():
			current = ''
			current_value = 0
			for letter in word:
				if letter.isalpha():
					current += letter
				if letter.isdigit():
					current_value += int(letter)
			dictionary[current] = current_value
dictionary['first'] = -1
redraw(field)

fra3 = Frame(root, width=300, height=50, bg="white", bd = 20)
lab_3 = Label(fra3, text = 'Выберите режим игры', font="Arial 18", bg = 'grey')
but_2 = Button(fra3)
but_2['text'] = 'С компьютером'
but_2['bg'] = 'blue'
but_2['fg'] = 'yellow'
but_2.bind('<Button-1>', game_with_computer)
but_1 = Button(fra3)
but_1['text'] = 'C человеком'
but_1['bg'] = 'blue'
but_1['fg'] = 'yellow'
but_1.bind('<Button-1>', game_with_man)
windows[0] = fra3



but.bind("<Button-1>",starter)


field.bind('<Button-3>', put_letter )
field.bind('<Motion>', mark)
field.bind('<Button-1>', start_or_end_marking)




lab_3.pack()
but_1.pack()
but_2.pack()
fra3.pack()
words_and_points.pack()



field.mainloop()
words_and_points.mainloop()
root.mainloop()
root_2.mainloop()
win.mainloop()