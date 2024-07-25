import math
import tkinter as tk
from tkinter import messagebox
import scipy.stats as stats


class ContingencyTable:
    def __init__(self, a: int, b: int, c: int, d: int):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def probability_of_observing_table(self):
        a, b, c, d = self.a, self.b, self.c, self.d

        if a < 0 or b < 0 or c < 0 or d < 0:
            return 0.0

        numerator = math.factorial(a + b) * math.factorial(c + d) * math.factorial(a + c) * math.factorial(b + d)
        denominator = (math.factorial(a) * math.factorial(b) * math.factorial(c) * math.factorial(d) *
                       math.factorial(a + b + c + d))

        return numerator / denominator


def the_fisher_exact_test_one_tailed(contingency_table: ContingencyTable):
    a, b, c, d = contingency_table.a, contingency_table.b, contingency_table.c, contingency_table.d
    p_value = ContingencyTable.probability_of_observing_table(contingency_table)

    if a <= b:

        for i in range(0, a):
            new_contingency_table = ContingencyTable(i, a + b - i, a + c - i, d - a + i)
            new_p_value = ContingencyTable.probability_of_observing_table(new_contingency_table)

            p_value += new_p_value

    else:

        for i in range(a + 1, a + c + 1):
            new_contingency_table = ContingencyTable(i, a + b - i, a + c - i, d - a + i)
            new_p_value = ContingencyTable.probability_of_observing_table(new_contingency_table)

            p_value += new_p_value

    return min(p_value, 1.0)


def the_fisher_exact_test_two_tailed(contingency_table: ContingencyTable):
    a, b, c, d = contingency_table.a, contingency_table.b, contingency_table.c, contingency_table.d
    p_value = ContingencyTable.probability_of_observing_table(contingency_table)

    if a == b == c == d:
        return 1.0

    result = p_value

    for i in range(a + c + 1):
        new_contingency_table = ContingencyTable(i, a + b - i, a + c - i, d - a + i)

        if new_contingency_table.a != a or new_contingency_table.c != c:
            new_p_value = ContingencyTable.probability_of_observing_table(new_contingency_table)

            if new_p_value <= p_value:
                result += ContingencyTable.probability_of_observing_table(new_contingency_table)

    return min(result, 1.0)


def calculate_fisher_exact_test():
    a, b, c, d = entry_a.get(), entry_b.get(), entry_c.get(), entry_d.get()

    if not all([a, b, c, d]):
        messagebox.showerror("Error", "Please enter all values.")
        return

    if not all([a.isdigit(), b.isdigit(), c.isdigit(), d.isdigit()]):
        messagebox.showerror("Error", "Please enter integer values.")
        return

    a, b, c, d = int(entry_a.get()), int(entry_b.get()), int(entry_c.get()), int(entry_d.get())

    if a > 100 or b > 100 or c > 100 or d > 100:
        messagebox.showerror("Error", "Please enter values less than or equal to 100.")
        return

    table = ContingencyTable(a, b, c, d)
    one_tailed_p_value = the_fisher_exact_test_one_tailed(table)
    one_tailed_p_value_correct = stats.fisher_exact([[a, b], [c, d]], alternative='less')
    two_tailed_p_value = the_fisher_exact_test_two_tailed(table)
    two_tailed_p_value_correct = stats.fisher_exact([[a, b], [c, d]], alternative='two-sided')

    one_tailed_display_box.delete(1.0, tk.END)
    one_tailed_display_box_correct.delete(1.0, tk.END)
    two_tailed_display_box.delete(1.0, tk.END)
    two_tailed_display_box_correct.delete(1.0, tk.END)
    one_tailed_display_box.insert(tk.END, f"{one_tailed_p_value:.4f}", 'center')
    one_tailed_display_box_correct.insert(tk.END, f"{one_tailed_p_value_correct[1]:.4f}", 'center')
    two_tailed_display_box.insert(tk.END, f"{two_tailed_p_value:.4f}", 'center')
    two_tailed_display_box_correct.insert(tk.END, f"{two_tailed_p_value_correct[1]:.4f}", 'center')


def main():
    global entry_cat1, entry_cat2, entry_cat3, entry_cat4
    global entry_a, entry_b, entry_c, entry_d
    global one_tailed_display_box, one_tailed_display_box_correct, two_tailed_display_box, two_tailed_display_box_correct

    m = tk.Tk()
    m.title("The Fisher's Exact Test")
    m.configure(bg='#70FF97')

    screen_width = m.winfo_screenwidth()
    screen_height = m.winfo_screenheight()
    window_width = 615
    window_height = 360
    position_x = int((screen_width - window_width) / 2)
    position_y = int((screen_height - window_height) / 2)
    m.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

    entry_cat1 = tk.Entry(m, justify='center', width=20, font=('Consolas', 12))
    entry_cat1.grid(row=1, column=1, padx=10, pady=10)
    entry_cat1.insert(0, "Category 1")

    entry_cat2 = tk.Entry(m, justify='center', width=20, font=('Consolas', 12))
    entry_cat2.grid(row=1, column=2, padx=10, pady=10)
    entry_cat2.insert(0, "Category 2")

    entry_cat3 = tk.Entry(m, justify='center', width=20, font=('Consolas', 12))
    entry_cat3.grid(row=2, column=0, padx=10, pady=10)
    entry_cat3.insert(0, "Category 3")

    entry_cat4 = tk.Entry(m, justify='center', width=20, font=('Consolas', 12))
    entry_cat4.grid(row=3, column=0, padx=10, pady=10)
    entry_cat4.insert(0, "Category 4")

    entry_a = tk.Entry(m, justify='center', width=20, font=('Consolas', 12))
    entry_a.grid(row=2, column=1, padx=10, pady=10)

    entry_b = tk.Entry(m, justify='center', width=20, font=('Consolas', 12))
    entry_b.grid(row=2, column=2, padx=10, pady=10)

    entry_c = tk.Entry(m, justify='center', width=20, font=('Consolas', 12))
    entry_c.grid(row=3, column=1, padx=10, pady=10)

    entry_d = tk.Entry(m, justify='center', width=20, font=('Consolas', 12))
    entry_d.grid(row=3, column=2, padx=10, pady=10)

    calc_button = tk.Button(m, text="Calculate P-Value", justify='center', width=20, font=('Consolas', 12),
                            command=calculate_fisher_exact_test)
    calc_button.grid(row=4, column=0, columnspan=3, pady=20)

    one_tailed_label = tk.Label(m, text="One-tailed (implemented)", font=('Consolas', 10))
    one_tailed_label.grid(row=5, column=0, padx=0, columnspan=2)

    one_tailed_display_box = tk.Text(m, height=1, width=20, font=('Consolas', 12))
    one_tailed_display_box.tag_configure('center', justify='center')
    one_tailed_display_box.grid(row=5, column=1, columnspan=3, padx=10)

    one_tailed_label = tk.Label(m, text="One-tailed (Python method)", font=('Consolas', 10))
    one_tailed_label.grid(row=6, column=0, padx=0, columnspan=2)

    one_tailed_display_box_correct = tk.Text(m, height=1, width=20, font=('Consolas', 12))
    one_tailed_display_box_correct.tag_configure('center', justify='center')
    one_tailed_display_box_correct.grid(row=6, column=1, columnspan=3, padx=10, pady=15)

    one_tailed_label = tk.Label(m, text="Two-tailed (implemented)", font=('Consolas', 10))
    one_tailed_label.grid(row=7, column=0, padx=0, columnspan=2)

    two_tailed_display_box = tk.Text(m, height=1, width=20, font=('Consolas', 12))
    two_tailed_display_box.tag_configure('center', justify='center')
    two_tailed_display_box.grid(row=7, column=1, columnspan=3, padx=10, pady=6)

    one_tailed_label = tk.Label(m, text="Two-tailed (Python method)", font=('Consolas', 10))
    one_tailed_label.grid(row=8, column=0, padx=0, columnspan=2)

    two_tailed_display_box_correct = tk.Text(m, height=1, width=20, font=('Consolas', 12))
    two_tailed_display_box_correct.tag_configure('center', justify='center')
    two_tailed_display_box_correct.grid(row=8, column=1, columnspan=3, padx=10, pady=10)

    m.mainloop()


if __name__ == "__main__":
    main()