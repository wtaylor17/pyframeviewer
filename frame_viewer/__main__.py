import argparse

try:
    import matplotlib.pyplot as plt
except:
    print('Matplotlib not found.')
    exit(1)

try:
    import imageio as iio
except:
    print('Imageio not found.')
    exit(1)


def launch_viewer(fd, verbose=True):
    frames = list(iio.get_reader(fd))
    
    if verbose:
        print('loaded', len(frames), 'frames from', fd)
    
    i = 0
    fig, axs = plt.subplots(1, 1)
    im = axs.imshow(frames[0])

    def on_press(event):
        nonlocal i, fig, im, verbose
        if event.key == 'a':
            i = (i - 1 + len(frames)) % len(frames)
            if verbose:
                print('On frame', i)
        elif event.key == 'd':
            i = (i + 1) % len(frames)
            if verbose:
                print('On frame', i)
        im.set_data(frames[i])
        fig.canvas.draw()

    fig.canvas.mpl_connect('key_press_event', on_press)
    plt.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=str)
    launch_viewer(parser.parse_args().input)
