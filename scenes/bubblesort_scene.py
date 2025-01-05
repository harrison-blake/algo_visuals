from manim import *

class BarChartBubbleSort(Scene):
    def construct(self):
        bar_values = [7, 4, 9, 11, 13, 1, 14, 2, 5]

        length = len(bar_values)
        for i in range(length):
            for j in range(1, length-i):
                chart = BarChart(
                    values = bar_values,
                    bar_colors = ["WHITE"],
                )

                self.add(chart)

                bar_a = chart.bars[j]
                bar_b = chart.bars[j-1]

                self.play(
                    bar_a.animate.set_fill(RED),
                    bar_b.animate.set_fill(RED),
                    run_time=0.1
                )

                self.wait(0.3)
                
                a_x = bar_a.get_bottom()
                b_x = bar_b.get_bottom()
                distance = a_x - b_x

                if(bar_values[j-1]>bar_values[j]):
                    self.play(
                        bar_a.animate.shift(-1 * distance),
                        bar_b.animate.shift(distance),
                        run_time=0.5
                    )

                    tmp = bar_values[j]
                    bar_values[j] = bar_values[j-1]
                    bar_values[j-1] = tmp
                    chart.change_bar_values(bar_values)

                self.remove(chart)


