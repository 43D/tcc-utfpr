import { PyUtilsType } from "../../../type/pywebview/index.d";


export const PyUtils = (util: PyUtilsType): PyUtilsType => {
    const save_file_dialog = (type_file: string, filename: string) => util.save_file_dialog(type_file, filename);
    const open_folder_if_exists = (path: string) => util.open_folder_if_exists(path);
    const check_file_exists = (filepath: string) => util.check_file_exists(filepath);
    const sleep_timer = (seconds: number) => util.sleep_timer(seconds);

    return {
        check_file_exists,
        open_folder_if_exists,
        save_file_dialog,
        sleep_timer
    }
}