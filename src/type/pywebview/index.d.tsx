export type PyDatabaseType = {
    get_attr: (tag: string) => Promise<string>;
    update_attr: (tag: string, value: string) => Promise<string>;
}

export type PyUtilsType = {
    save_file_dialog: (type_file: string, filename: string) => Promise<string | null>;
    open_folder_if_exists: (path: string) => Promise<null>;
    check_file_exists: (filepath: string) => Promise<boolean>;
    sleep_timer: (seconds: number) => Promise<true>;
}


export type PywebviewApiType = {
    databaseController: PyDatabaseType;
    utils: PyUtilsType;
}

export interface pywebview {
    api: PywebviewApiType;
};