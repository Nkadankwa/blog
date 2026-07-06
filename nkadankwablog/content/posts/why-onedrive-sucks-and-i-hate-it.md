+++
date = '2026-07-06T09:00:00+08:00'
image = '/images/cloud-storage-editorial.png'
title = 'Why OneDrive sucks and I hate it'
categories = ['My Two Cents']
tags = ['OneDrive', 'Windows', 'Cloud Storage']
+++

OneDrive is one of the most irritating parts of Windows for me. My problem begins with how deeply it tries to place itself inside an ordinary local workflow.

I want the location of a file to be obvious. A document saved on my laptop should stay where I chose to save it. OneDrive can redirect familiar folders such as Desktop and Documents into its own folder when folder backup is enabled. File Explorer still presents those locations in a familiar way, so the change can be easy to miss until syncing pauses, storage fills up, or a file appears somewhere unexpected.

## Sync makes deletion travel

The deletion behaviour makes this worse. Microsoft explains that additions, changes, and deletions inside a synced OneDrive folder propagate between the computer and the cloud. A file deleted from OneDrive can therefore disappear from the synced folder on the PC as well. Recovery may be possible through a recycle bin, but the design still violates the simple mental model I want: cloud storage should hold a copy without quietly taking control of the original.

Keeping a local file while removing its cloud copy requires moving it outside the OneDrive folder first. That rule makes sense once the sync model is understood. Windows does a poor job of ensuring that every user understands the model before their important folders become part of it.

## An app I removed should stay removed

I also resent software that returns after I have uninstalled it. OneDrive is presented as removable, yet Windows integration and later setup or update experiences can make it feel persistent. I should not have to repeatedly defend a decision to keep local folders local.

OneDrive can be useful for people who want the same files across devices. My frustration comes from the pressure, unclear folder ownership, and consequences that reach beyond the cloud. A sync service should earn its place through clear consent and predictable controls. OneDrive has repeatedly made me feel that Windows made the choice first.

Sources: [Microsoft on OneDrive syncing](https://support.microsoft.com/en-us/onedrive/sync-your-computer-s-files-and-folders-with-onedrive) and [deleting synced files](https://support.microsoft.com/en-us/onedrive/delete-files-or-folders-in-onedrive).
