import random
import matplotlib.pyplot as plt

def data():
    paths = {}
    line_style = input("Enter line style (':', '--', or '-'):") #line style
    color = input("Enter color ('r' for red, 'g' for green, 'b' for blue):") #color
    marker = input("Enter marker style ('o', 's', or '^'):") #marker style
    #Store in dictionary
    paths['line'] = line_style
    paths['color'] = color
    paths['marker'] = marker

    return paths

def generate():
    #number of lines
    num_lines = int(input("How many lines would you like to display?"))
    for i in range(num_lines):
        #Get user preferences
        values = data()
        #Generate random x and y values
        x = random.sample(range(1, 21), 10)
        y = random.sample(range(1, 21), 10)
        #Plot the line with specified styles
        plt.plot(x, y, linestyle=values['line'], color=values['color'], marker=values['marker'], label=f'Line {i+1}')

    # Add legend and display the plot
    plt.legend()
    plt.title("User-Defined Line Plots")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)
    plt.show()

def run():
    print("Running....")
    generate()
    print("Done!")

if __name__ == "__main__":
    run()
