
def normalize_formats(filepaths):
    pass

def split_stereo(input_file, output_file_left, output_file_right):
    """Split a stereo file into separate mono files.

    Parameters
    ----------
    input_file : str
        Path to stereo audio file.
    output_file_left : str
        Path to output of left channel.
    output_file_right : float
        Path to output of right channel.

    Returns
    -------
    status : bool
        True on success.

    """
    left_args = ['sox', '-D', input_file, output_file_left, 'remix', '1']
    right_args = ['sox', '-D', input_file, output_file_right, 'remix', '2']
    return sox(left_args) and sox(right_args)


def multimono_to_stereo(left_channel, right_channel, output_file):
    """Create a stereo audio file from the 2 mono audio files.
    Left goes to channel 1, right goes to channel 2.

    Parameters
    ----------
    left_channel : str
        Path to mono audio file that will be mapped to the left channel.
    right_channel : str
        Path to mono audio file that will be mapped to the right channel.
    output_file : float
        Path to stereo output file.

    Returns
    -------
    status : bool
        True on success.

    """
    return sox(['sox', '-M', left_channel, right_channel, output_file])


def mix_weighted(file_list, weights, output_file):
    """Naively mix (sum) a list of files into one audio file.
    Volume of each file is set by the value in weights.

    Parameters
    ----------
    file_list : list
        List of paths to audio files.
    weights : list
        List of mixing weights.
    output_file : str
        Path to output file.

    Returns
    -------
    status : bool
        True on success.
    """
    args = ["sox", "-m"]
    for fname, weight in zip(file_list, weights):
        args.append("-v")
        args.append(str(weight))
        args.append(fname)
    args.append(output_file)

    return sox(args)


def mix(file_list, output_file):
    """Naively mix (sum) a list of files into one audio file.

    Parameters
    ----------
    file_list : list
        List of paths to audio files.
    output_file : str
        Path to output file.

    Returns
    -------
    status : bool
        True on success.
    """
    args = ["sox", "-m"]
    for fname in file_list:
        args.append(fname)
    args.append(output_file)

    return sox(args)


def concatenate(file_list, output_file):
    """Concatenate a list of files into one audio file.

    Parameters
    ----------
    file_list : list
        List of paths to audio files.
    output_file : str
        Path to output file.

    Returns
    -------
    status : bool
        True on success.
    """
    args = ["sox", "--combine"]
    args.append("concatenate")
    for fname in file_list:
        args.append(fname)
    args.append(output_file)

    return sox(args)