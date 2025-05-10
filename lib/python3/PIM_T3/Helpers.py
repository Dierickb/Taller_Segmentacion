def SplitPath(path):
    path_dir = path.split("/")
    path_dir, file_name = path_dir[:-3], path_dir[-1].split(".")[0]
    path_dir = "/".join(path_dir)
    return path_dir, file_name


def ImagePath(path, file_executed=None):

    output_dir = path.split("/")
    output_dir, file_name = output_dir[:-1], output_dir[-1].split(".")[0]

    output_dir_aux = output_dir[:-1]
    output_dir_aux = "/".join(output_dir_aux)

    if file_executed is not None:
        file_executed = SplitPath(file_executed)
        output_dir_aux = f"{output_dir_aux}/{file_executed[1]}/{file_name}.nii"
        return output_dir_aux

    return f"{output_dir_aux}/images/{output_dir[-1]}/{file_name}.nii"